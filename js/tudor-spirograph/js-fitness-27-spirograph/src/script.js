Object.getOwnPropertyNames(Math).map(function(p) {
  window[p] = Math[p];
});

var rand = function(min, max, isInt) {
  var max = ((max - 1) || 0) + 1, 
      min = min || 0, 
      gen = min + (max - min)*random();
    
  return (isInt)?(~~gen):gen;
};

var randsign = function() {
  return (random() < .5)?-1:1;
};

var c = document.querySelectorAll('.c'), 
    w, h, min_dim, ctx =[], 
    ctrls = document.querySelector('.controls'), 
    ctrl_c = 'hsl(84, 99%, 69%)', 
    r1_ctrl = document.getElementById('r1'), 
    r1, r1_f, r1_c = 'hsl(328, 100%, 75%)', 
    r2_ctrl = document.getElementById('r2'), 
    r2, r2_f, r2_c = 'hsl(60, 100%, 75%)', 
    sign, r2_rot, r2_r, 
    trace_ctrl = document.getElementById('d'), 
    d, d_f, 
    hue_ctrl = document.getElementById('hue'), 
    hue, 
    trace_c, 
    hypo_ctrl = document.getElementById('hypo'), 
    epi_ctrl = document.getElementById('epi'), 
    v_ctrl = document.getElementById('v'), 
    v_f, 
    rand_ctrl = document.getElementById('rand'), 
    ok_ctrl = document.getElementById('apply'), 
    no_ctrl = document.getElementById('cancel'), 
    toggle = document.getElementById('toggle'),
    prev_pos = null, 
    theta = 0, u = PI/180;
    t = 0, rID = null, running = false;

var setUpCanvas = function() {
  var s = getComputedStyle(c[0]);
  
  w = ~~s.width.split('px')[0];
  h = ~~s.height.split('px')[0];
  min_dim = min(w, h);
  
  for(var i = 0; i < 3; i++) {
    c[i].width = w;
    c[i].height = h;
    ctx[i] = c[i].getContext('2d');
    ctx[i].lineWidth = 3;
    ctx[i].translate(w/2, h/2);
  }
  
  initValues();
};

var initValues = function() {
  r1_f = 1*r1_ctrl.value;
  r2_f = 1*r2_ctrl.value;
  d_f = 1*trace_ctrl.value;
  v_f = 1*v_ctrl.value;
  
  sign = (hypo_ctrl.checked)?-1:1;
  hue = ~~hue_ctrl.value;
  trace_c = 'hsl(' + hue + ', 100%, 56%)'
  
  r1 = r1_f*min_dim/2;
  r2 = r2_f*r1;
  d = d_f*r2;
  
  r2_rot = r1 + sign*r2;
  r2_r = r2_rot/r2;
  
  if(rID) {
    cancelAnimationFrame(rID);
    t = 0;
    theta = 0;
    prev_pos = null;
    
    for(var i = 0; i < 3; i++) {
      ctx[i].clearRect(-w/2, -h/2, w, h);
    }
  }
  
  styleSlider(r1_ctrl);
  styleSlider(r2_ctrl);
  styleSlider(trace_ctrl);
  styleSlider(v_ctrl);
  
  drawFixed();
  ctx[2].strokeStyle = trace_c;
  ani();
};

var resetValues = function() {
  r1_ctrl.value = r1_f;
  r2_ctrl.value = r2_f;
  trace_ctrl.value = d_f;
  v_ctrl.value = v_f;
  
  hypo_ctrl.checked = (sign < 0)?true:false;
  epi_ctrl.checked = (sign > 0)?true:false;
  
  hue_ctrl.value = hue;
  
  styleSlider(r1_ctrl);
  styleSlider(r2_ctrl);
  styleSlider(trace_ctrl);
  styleSlider(v_ctrl);
};

var randValues = function() {
  var tmps = randsign();
  
  r1_ctrl.value = rand(1*r1_ctrl.max, 1*r1_ctrl.min).toFixed(2);
  r2_ctrl.value = rand(1*r2_ctrl.max, 1*r2_ctrl.min).toFixed(2);
  trace_ctrl.value = rand(1*trace_ctrl.max, 1*trace_ctrl.min).toFixed(2);
  v_ctrl.value = rand(1*v_ctrl.max, 1*v_ctrl.min).toFixed(2);
  
  hypo_ctrl.checked = (tmps < 0)?true:false;
  epi_ctrl.checked = (tmps > 0)?true:false;
  
  hue_ctrl.value = ~~rand(1*hue_ctrl.max, 1*hue_ctrl.min);
  
  styleSlider(r1_ctrl);
  styleSlider(r2_ctrl);
  styleSlider(trace_ctrl);
  styleSlider(v_ctrl);
};

var drawFixed = function() {
  ctx[0].strokeStyle = r1_c;
  ctx[0].beginPath();
  ctx[0].moveTo(r1, 0);
  ctx[0].arc(0, 0, r1, 0, 2*PI);
  ctx[0].closePath();
  ctx[0].stroke();
};

var drawRoller = function(pc, pt) {
  var pc = { 'x': round(pc.x), 'y': round(pc.y) };
  
  ctx[1].clearRect(-w/2, -h/2, w, h);
  ctx[1].strokeStyle = r2_c;
  ctx[1].beginPath();
  ctx[1].moveTo(pc.x + r2, pc.y);
  ctx[1].arc(pc.x, pc.y, r2, 0, 2*PI);
  ctx[1].moveTo(pc.x + 2, pc.y);
  ctx[1].arc(pc.x, pc.y, 2, 0, 2*PI);
  ctx[1].moveTo(pc.x, pc.y);
  ctx[1].lineTo(pt.x, pt.y);
  ctx[1].closePath();
  ctx[1].stroke();
  
  ctx[1].strokeStyle = trace_c;
  ctx[1].beginPath();
  ctx[1].moveTo(pt.x, pt.y);
  ctx[1].arc(pt.x, pt.y, 3, 0, 2*PI);
  ctx[1].closePath();
  ctx[1].stroke();
};

var drawTracer = function(pt) {  
  if(prev_pos) {
    ctx[2].beginPath();
    ctx[2].moveTo(prev_pos.x, prev_pos.y);
    ctx[2].lineTo(pt.x, pt.y);
    ctx[2].closePath();
    ctx[2].stroke();
  }
  
  prev_pos = {'x': pt.x, 'y': pt.y};
};

var ani = function() {
  var pc, pt, j, k;
  
  if(running) {
    theta = v_f*t/60*2*PI/((r2_rot + d)/128);

    pc = {
      'x': r2_rot*cos(theta), 
      'y': r2_rot*sin(theta)
    };

    pt = {
      'x': round(pc.x - sign*d*cos(theta*r2_r)), 
      'y': round(pc.y - d*sin(theta*r2_r))
    };

    drawRoller(pc, pt);
    drawTracer(pt);
  }
  
  t++;
  
  j = floor(theta/PI);
  k = theta - j*PI;
  
  if(running && abs(theta) > PI && 
     abs(k) < 5*u && t > 1 && 
     abs(r2_rot - sign*d - pt.x) < 8 && 
     abs(pt.y) < 8) {
    running = false;
    
    pc = { 'x': r2_rot, 'y': 0 };
    pt = { 'x': r2_rot - sign*d, 'y': 0 };
    
    drawRoller(pc, pt);
    drawTracer(pt);
    
    t = 0;
  }
  else { if(running) { running = true; } }
  
  if(!running && t > 30) {
    ctx[2].clearRect(-w/2, -h/2, w, h);
    running = true;
    t = 0;
  }
  
  rID = requestAnimationFrame(ani);
};

var styleSlider = function(me, pre) {
  var span = me.max - me.min, 
      rel_val = (me.value - me.min)/span, 
      perc = round(rel_val*100), 
      txt_val = 'linear-gradient(90deg, ' + 
        ctrl_c + ' ' + perc + '%, grey ' + perc + '%)';
  
  me.style.background = txt_val;
};

setTimeout(function() {
  setUpCanvas();
  
  addEventListener('resize', setUpCanvas, false);
  
  r1_ctrl.addEventListener('input', function() {
    styleSlider(this);
  }, false);
  
  r1_ctrl.addEventListener('change', function() {
    styleSlider(this);
  }, false);
  
  r2_ctrl.addEventListener('input', function() {
    styleSlider(this);
  }, false);
  
  r2_ctrl.addEventListener('change', function() {
    styleSlider(this);
  }, false);
  
  trace_ctrl.addEventListener('input', function() {
    styleSlider(this);
  }, false);
  
  trace_ctrl.addEventListener('change', function() {
    styleSlider(this);
  }, false);
  
  v_ctrl.addEventListener('input', function() {
    styleSlider(this);
  }, false);
  
  v_ctrl.addEventListener('change', function() {
    styleSlider(this);
  }, false);
  
  rand_ctrl.addEventListener('click', randValues, false);
  ok_ctrl.addEventListener('click', function() {
    initValues();
    ctrls.classList.remove('controls--open');
  }, false);
  no_ctrl.addEventListener('click', resetValues, false);
  
  toggle.addEventListener('click', function() {
    ctrls.classList.toggle('controls--open');
  }, false);
}, 15);