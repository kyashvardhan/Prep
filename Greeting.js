/* 🟢 Problem 2: Function to Return a Greeting
💡 Task: Write a function greetUser() that takes a name and returns "Hello, [name]!".
✅ Use Template Literals (`Hello ${name}`). */

let name = prompt("What is your name..?");

function greetUser(){
    return `Hello ${name}`;
}
console.log(greetUser());