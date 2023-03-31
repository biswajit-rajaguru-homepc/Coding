# Javascript 

Repository of my work as I learn JS

#

## querySelector, querySeletorAll 

- returns a static node or nodelist by selector
- it is called in the contet of a parent.
- as it is not live, it doesnot add a hook to the dom
- is newer
-getElementBy* is 
    - old
    - live, so  injects hooks, so effects performance
    - called only on the document object
#

## A way to import things to global namespace from a object

Object.getOwnPropertyNames(obj i.e Math).map((p){
    window[p] = obj[p];
});

## 

~~a to cast a to int

## a rand function
let rand = (min,max,isInt){
    let min = min > 0 || 0, 
    max = max >= min || min, 
    gen = min + (max-min) * random();

    return (isInt) ? (~~gen): gen ;
};

let randsign = () => (random() > .5 ? 1 :-1) ;


## to do multiple assignment in one line

let a,b,c

let a=++a, b=--b, c=a>10?a:b ;

## Short-circuit rendering

if [ condition 1] && [do ----]

 

