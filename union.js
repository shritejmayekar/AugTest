
let a=[1,2,3]
let b=[100,2,1,10]
let c=[]


const union = () =>{
    for(let i=0;i<a.length;i<i++){
      if(!c.includes(a[i])) {
        c.push(a[i])
      }
    }
    for(let i=0;i<b.length;i<i++){
      if(!c.includes(b[i])) {
        c.push(b[i])
      }
    }
    return c;
}

console.log(union([1, 2, 3], [100, 2, 1, 10]))
