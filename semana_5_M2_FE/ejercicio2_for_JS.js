const list1=[1,2,3,4,5,6,7,8,9,10];
let list2 = [];


for (let i=0; i<list1.length;i++){
    if (list1[i]%2===0){
        list2.push(list1[i]);
        
    }
}

console.log(list2);


