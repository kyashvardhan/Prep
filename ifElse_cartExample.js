/* If the cart value is above ₹500, you give free shipping.
If the cart value is below ₹500, the user has to pay ₹50 shipping.
If the cart is empty (₹0), show a message: "Your cart is empty." */

var cart = 0;

if(cart===0){
    console.log("Cart is Empty");
} else if(cart<500){
    console.log("You Pay 50 Rupees");
} else{
    console.log("You Get free shipping");
}