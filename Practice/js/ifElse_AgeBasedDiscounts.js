/*Problem 3: Age-Based Discounts
💡 Write a function getTicketPrice() that takes an age and returns the ticket price.
✅ Below 5 years → Free Ticket (₹0)
✅ 5-12 years → Child Ticket (₹100)
✅ 13-59 years → Adult Ticket (₹200)
✅ 60+ years → Senior Ticket (₹150)*/

function getTicketPrice(age){
    if(age<5){
        return 'You get Free Ticket';
    }else if(age>=5 && age<=12){
        return'Your Ticket Price is 100 rupees'
    }else if(age>=13 && age<=59){
        return'Your Ticket Price is 200 rupees'
    }else{
        return'Your Ticket Price is 150 rupees'
    }
}
console.log(getTicketPrice(3)); // "₹0 (Free Ticket)"
console.log(getTicketPrice(10)); // "₹100 (Child Ticket)"
console.log(getTicketPrice(30)); // "₹200 (Adult Ticket)"
console.log(getTicketPrice(65)); // "₹150 (Senior Ticket)"

