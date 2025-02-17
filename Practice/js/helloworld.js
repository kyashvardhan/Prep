//just print
console.log("Hello World - Classic");

//using function
function hello(){
    return 'hello world';
}
console.log("printed using function :"+ hello());

//Immediately Invoked Function Expression (IIFE)
(function() {
    console.log("Hello, JavaScript! (IIFE)");
})();

//Using Arrow Functions
const helloArrow = () => "Hello, JavaScript! (Arrow Function)";
console.log(helloArrow());

//Template Literals backticks (` `).
console.log(`Hello, JavaScript! (Template Literal)`);

setTimeout(() => console.log("Hello, JavaScript! (After 2 Seconds)"), 2000);
