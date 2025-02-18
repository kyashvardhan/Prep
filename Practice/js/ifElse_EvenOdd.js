/*🟢 Problem 1: Check Even or Odd
💡 Write a function isEven() that checks if a number is even or odd.
✅ If even, return "Even"
✅ If odd, return "Odd"*/

/* var enternum = Number(prompt('Enter Number'));
//var enternum = 20;
if(enternum%2===0){
    console.log('Number is Even');
}else{
    console.log("Number is Odd");
}
*/

/* function isEven(){
    if(isEven%2===0){
        console.log('Number is Even');
    }else{
        console.log("Number is Odd");
    }
}

console.log(isEven(4)); // "Even"
console.log(isEven(7)); // "Odd"
*/

function isEven(num) {  // Accept a number as an argument
    if (num % 2 === 0) {
        return 'Number is Even';
    } else {
        return "Number is Odd";
    }
}

console.log(isEven(4)); // ✅ "Number is Even"
console.log(isEven(7)); // ✅ "Number is Odd"
