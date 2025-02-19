/* 
var letter = ('Hello');
// 1️⃣ Convert the string into an array (split('')).
//console.log(letter);

var myNewLetter = letter.split(" ", 2);
//var word = myNewLetter[3];
console.log(myNewLetter);

*/

function reverseString(str){
    return str.split("").reverse().join("");
}

console.log(reverseString("helloooo"));
console.log(reverseString("JavaScript"));