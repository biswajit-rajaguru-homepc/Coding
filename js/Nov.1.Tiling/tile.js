
function main() {
    const c = document.getElementById('tile');
    const ctx = c.getContext('2d')
    
    c.width = 512
    c.height = 512
    const width = c.width, height = c.height
    const tileWidth = 512, tileHeight  = 512
    const tileOx = Math.floor(width/2 -256), tileOy = Math.floor(height/2 -256)
    
    console.log(' ')
    let n = 7
    let style = 'diagonal'
    let step = 512/Math.pow(2,n-1) 
    for (let x = 0; x < 512; x += step) {
        for (let y = 0; y < 512; y += step) {
            if (Math.random() > 0.2) {
                
                switch(style){
                    case 'diagonal':
                        ctx.moveTo(x,y)
                        ctx.lineTo(x+step,y+step)
                        break

                    case 'straight':
                        ctx.moveTo(x+step/2,y)
                        ctx.lineTo(x+step/2,y+step)
                        break

                    default:
                }

            } else {

                
                switch(style){
                    case 'diagonal':
                        ctx.moveTo(x,y+step)
                        ctx.lineTo(x+step,y)
                        break

                    case 'straight':
                        ctx.moveTo(x,y+step/2)
                        ctx.lineTo(x+step,y+step/2)
                        break
                    
                    default :


                }
                

            }
            
        }
     
        
    }

    ctx.stroke();

}

window.addEventListener("load",main);