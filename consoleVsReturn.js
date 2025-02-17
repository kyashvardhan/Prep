/* function add(a, b) {
    console.log(a + b);
}

let sum = add(5, 3);
console.log(sum); // ❌ Output: undefined


function add(a, b) {
    return a + b;
}
let sum = add(5, 3);
console.log(sum); // ✅ Output: 8 

function test() {
    console.log("Before return");
    return "Hello!";
    console.log("After return"); // ❌ This will NEVER run
}

console.log(test());
// ✅ Output:
// "Before return"
// "Hello!"

function multiply(a, b) {
    console.log(a * b); // ❌ This just prints the value
}

let result = multiply(4, 5);
console.log(result); // 

function multiply(c, d) {
    return c * d; // ✅ Now it returns a value
}

let resultr = multiply(4, 5);
console.log(resultr); // ✅ Output: 20 

function getMessage() {
    return "Hello!";
}

console.log(getMessage); // ❌ Output: function getMessage()
console.log(getMessage()); // ✅ Output: "Hello!"


function getNumber() {
    console.log(100); // ❌ Prints but does NOT return
}

let num = getNumber();
console.log(num); // ❌ Output: undefined 

function getNumber() {
    return 100; // ✅ Now it returns a value
}

let num = getNumber();
console.log(num); // ✅ Output: 100 */

function getDouble(num) {
    return (num * 2);
}

let result = getDouble(5);
console.log(result); // ❌ Fix this!



