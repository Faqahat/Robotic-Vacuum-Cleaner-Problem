let size =4;
// /let arr = [
//     [3 , 9 , 2 , 5],
//     [0 , 1 , 0 , 6],
//     [3 , 8 , 7 , 2],
//     [4 , 6 , 5 , 1]
    
//    ];
// let arra = [
//     [3 , 3 , 10 , 5],
//     [0 , 3 , 20 , 6],
//     [3 , 8 , 7 , 2],
//     [4 , 6 , 5 , 1]
    
//    ];
/*

5621797533863034
5.6.2.1.10.20.7.5.3.3.8.6.3.0.3.4

let  input=  "445629997533863034"
let arr = [];
let size;
*/
let arr = [
    [5 , 6 , 2 , 1],
    [1 , 0 , 7 , 5],
    [9 , 1 , 8 , 6],
    [3 , 0 , 3 , 4]
    
   ];


 let highest = {
     sum : 0
 };
 for(let x = 0; x < size  ; x++) 
 {
    for(let y = 0; y < size  ; y++) 
    {
        let sum;
        if(x + 1  <  size && x  <  size &&  y  <  size && y + 1  <  size)
        {
            sum = arr[x][y]  + arr[x+1][y] + arr[x][y+1] + arr[x+1][y+1];
            if(highest.sum < sum)
            highest = { a : x  , b : x+1 , c : y , d : y+1 , sum : sum }

        }
    }
}
console.log(
    
    "(", highest.a , "," , highest.c , ")" , 
    "(", highest.b , "," , highest.c , ")",
    "(", highest.a , "," , highest.d , ")",
    "(", highest.b , "," , highest.d , ") " ,
    highest.sum
 )

