const veryPromise = new Promise ((resolve)=>{
setTimeout(()=>resolve ("very"), 3000);

});

const dogsPromise = new Promise ((resolve)=>{
    setTimeout(()=>resolve ("Dogs"), 1000);
    
});

const cutePromise = new Promise ((resolve)=>{
    setTimeout(()=>resolve ("cute"), 4000);
    
});

const arePromise = new Promise ((resolve)=>{
    setTimeout(()=>resolve ("are"), 2000);
    
});


Promise.all([dogsPromise,arePromise ,veryPromise, cutePromise])
.then ((words)=>{
    console.log(words.join(" "));
});