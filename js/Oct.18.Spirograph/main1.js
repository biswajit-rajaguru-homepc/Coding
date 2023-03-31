
let r1,r2;


function drawSpirograph() {
    const cnv = document.getElementById('c1');
    const ctx = c1.getContext('2d') 
    ctx.fillstyle='green';
    cnv.style.width='100%';
    cnv.style.height='100%';
    cnv.width=cnv.offsetWidth;
    cnv.height=cnv.offsetHeight;
    const cx = cnv.width/2, cy = cnv.height/2;
    const s = cx/2 ;
    r1 = Math.random();
    r2 = Math.random();
    ctx.strokeStyle="rgb(0,255,0)";
    ctx.clearRect(0,0,cnv.width,cnv.height);
    let x,y,x0,y0,theta1,theta,a,b,px,py,dx,dy,pdx,pdy;
    pdx = cx + s*(1-r1);
    pdy = cy - s*(r2);
    ctx.moveTo(pdx,pdy);
    for (theta = 0; theta < 130; theta += 0.01) {
        x=Math.cos(theta);
        y=Math.sin(theta);
        x0=x;
        y0=y;
        // x *= -1;
        // y *= -1;
        theta1 = ((-1.0)*theta)/r1;
        a=r2*Math.cos(theta1);
        b=r1+r2*Math.sin(theta1);
        px = x0 - a*y - b*x;
        py = y0 + a*x -b*y;
        dx = cx + s*px;
        dy = cy - s*py ;
        
        ctx.lineTo(dx,dy);
        pdx = dx;
        pdy = dy;
       


    
    }
    ctx.stroke();
}
window.addEventListener('load',drawSpirograph);
const drawB = document.getElementById('drawB');
//console.log(drawB);
drawB.addEventListener('click',drawSpirograph);