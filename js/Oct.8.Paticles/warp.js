
let globalID, state = false, effect ;

function animate(){
    effect.update();
    effect.draw();
    globalID = requestAnimationFrame(animate);

}



window.addEventListener('load', function(){
    const c1 = document.getElementById('c1');
    const ctx = c1.getContext('2d');
    c1.width = window.innerWidth;
    c1.height = window.innerHeight;
    const img1 = document.getElementById('img1');


    class Particle {
        constructor(effect, x, y, color) {
            this.x = x;
            this.y = y;
            this.originX = Math.floor(x);
            this.originY = Math.floor(y);
            this.vx = Math.random()*5.0 - 2.5;
            this.vy = Math.random()*5.0 - 2.5;
            this.effect = effect;
            this.context = this.effect.context;
            this.color = color;
            this.size = this.effect.gap;
        }

        draw() {
            this.context.fillStyle = this.color ;
            this.context.fillRect(Math.floor(this.x), Math.floor(this.y), this.size, this.size);
        }

        update() {
            if ((this.x <= 0) || (this.x >= this.effect.width)) this.vx *= -1.0
            if ((this.y <= 0) || (this.y >= this.effect.height)) this.vy *= -1.0
            this.x += this.vx;
            this.y += this.vy;
        }
    }

    class Effect {
        constructor(context, width, height) {
            this.width = width;
            this.height = height;
            this.particlesArray = [];
            this.context = context;
            this.img1 = document.getElementById('img1');
            this.centerX = this.width * 0.5;
            this.centerY = this.height * 0.5;
            this.imgx = this.centerX - this.img1.width * 0.5;
            this.imgy = this.centerY - this.img1.height * 0.5;
            this.gap = 2;
            this.speed = 0.05;
        }

        mrndn = (n) => Math.floor(Math.random() * n) ;
        mrnd = (n) => Math.random() * n ;
        

        init() {
            //#region 
            // for (let i = 0; i < 20; i++) {
            //     this.particlesArray.push(new Particle(this,this.mrndn(this.width), 
            //     this.mrndn(this.height),this.mrndn(20),this.mrndn(5), this.mrndn(5)));
            // }   
            //#endregion
            this.context.drawImage(this.img1,this.imgx, this.imgy);
            const pixels = this.context.getImageData(0, 0, this.width, this.height).data;
            //console.log(pixels);
            for (let j = 0; j < this.height ; j += this.gap) {
                for (let i = 0; i < this.width; i+= this.gap) {
                    
                    const index = (j*this.width + i)*4;
                    const red = pixels[index];
                    const green = pixels[index+1];
                    const blue = pixels[index+2];
                    const alpha = pixels[index+3];
                    const color = 'rgb(' + red + ',' + green + ',' + blue + ')'; 

                    if(alpha > 0) {
                        this.particlesArray.push(new Particle(this, i, j, color));
                    }
                }
            }
            console.log(this.particlesArray.length);
            const warpb = document.getElementById('warpb');
            console.log(warpb)
            warpb.addEventListener('click', this.warp)
        }

               

        draw(){
            this.context.clearRect(0, 0, this.width, this.height);
            this.particlesArray.forEach(particle => particle.draw());
        }

        update(){
            this.particlesArray.forEach(particle => {
                
                particle.x += ((particle.originX - particle.x) * this.speed) ;
                particle.y += ((particle.originY - particle.y) * this.speed) ;
                //particle.update();
                
            
            });
            
        }

        warp(){
            this.particlesArray.forEach(particle => {
                particle.x = Math.floor(Math.random() * this.width);
                particle.y = Math.floor(Math.random() * this.height);
            });
        }
    }

    effect = new Effect(ctx, c1.width, c1.height);
    
    effect.init();
      

});



//#region 
function moveImage() {
    const c1 = document.getElementById('c1');
    const ctx = c1.getContext('2d');
    const img1 = document.getElementById('img1');
    
    ctx.clearRect(0, 0, c1.width, c1.height);
    const myrand = (n) => Math.floor(Math.random()*n); 
    ctx.drawImage(img1,myrand(c1.width),myrand(c1.height),200,150);

}

function toggleAnimation() {
    
    state = !state ;
    
    if(state) {
        window.animate();
    } else {
        cancelAnimationFrame(globalID);
    }

    

}

//#endregion