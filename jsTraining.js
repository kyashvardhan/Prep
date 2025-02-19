let cart = ["Apple", "Banana", "Mango"];
console.log(cart); 
console.log("------------------------------")
// Output: ["Apple", "Banana", "Mango"]

cart.push('Orange');
console.log(cart);
console.log("------------------------------")
// Output: ["Apple", "Banana", "Mango", "Orange"]

cart.pop();
console.log(cart);
console.log("------------------------------")
// Output: ["Apple", "Banana", "Mango"]

// map() – Modify every item in an array
let prices = [10, 20, 30];
let newPrices = prices.map(price => price * 2);
console.log(newPrices);
console.log("------------------------------")
// Output: [20, 40, 60]

//filter() – Select only specific items
let numbers = [10, 15, 20, 25];
let evenNumber = numbers.filter(num => num % 2 ===0);
console.log(evenNumber);
console.log("------------------------------")

//Objects
let user = {
    name: "Ayush", // key value
    age: 25,
    country: "India"
};
console.log(user.name); 
console.log(Object.keys(user)); 
console.log(Object.values(user));
console.log(Object.entries(user)); 
console.log("------------------------------")

// Arrow functions (=>) are just a shorter way to write functions in JavaScript. That’s it!
const greet = (name) => "Hello " + name;
console.log(greet('yash'));

function greet1(name1){
    return "bye"+name1;
}
console.log(greet1(' yash')); 
console.log("------------------------------")

// Strings & String Methods
let message = "Watch, Money Heist!";
console.log(message); 

console.log(message.length);
console.log(message.toUpperCase()); 

console.log(".............")
let words = message.split(" "); 
console.log(words); 