const class1 = document.querySelector('.class')
const id1 = document.querySelector('#id1')
const id2 = document.getElementById('id2')
const stopwatch = document.getElementById('stopwatch')
stopwatch.style.fontSize = "100px"
stopwatch.style.textAlign = 'center'
stopwatch.style.background = '#0000ff'
stopwatch.style.color = '#ffffff'
stopwatch.style.width = '50%'
stopwatch.style.left = '25%'
let cntr_on = false
let seconds = 0
let interval = 200
document.getElementById('b1').addEventListener('click', changed)
document.getElementById('b2').addEventListener('click', function () { 
    id2.textContent += 'hello '
})

document.getElementById('b3').addEventListener('click', start_watch)
function stop_watch() {
    seconds += 1
    let hours = Math.floor(seconds / 3600)
    let mins = Math.floor((seconds % 3600) / 60)
    let secs = seconds % 60
    let display = hours.toString() + ":" + mins.toString() + ":" + secs.toString()
    stopwatch.textContent = display
}

function start_watch() {
    seconds = 0
    if (!cntr_on) {
        setInterval(stop_watch, 10)
        cntr_on = true
    }
    
}


function changed() {
    class1.textContent = "Changed"
    id1.textContent = "Changed -"
    id2.textContent = "Changed +"
}