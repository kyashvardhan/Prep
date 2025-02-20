/* Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video goes into more detail.

This is how to work out whether if a particular year is a leap year:
- A year is a leap year if it is evenly divisible by 4 ;
- except if that year is also evenly divisible by 100;
- unless that year is also evenly divisible by 400. */

var year= prompt("Enter The Year");
year = Number(year);

if (year % 4 !==0){
    console.log('Its Not an Leap Year');
}
    else if(year%100 !==0){
        console.log('Its an Leap Year');
    }
    else if(year%400 ===0){
        console.log('Its an Leap Year');
    }
else{
    console.log('Its Not an Leap Year');
}