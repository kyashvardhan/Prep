/* Problem 4: Login System
💡 Write a function login() that takes a username and password and returns a message:
✅ "Login successful!" if username = "admin" and password = "1234".
✅ "Invalid username or password." if incorrect details are entered. */

function login(user,pass){
    if(user==='admin' && pass==='1234'){
        return'Login successful!';
    }else{
        return'Invalid username or password';
    }
}

console.log(login("admin", "1234")); // "Login successful!"
console.log(login("user", "pass")); // "Invalid username or password."