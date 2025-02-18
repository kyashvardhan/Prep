/*Write a function getGrade() that takes a score (0-100) and returns the grade.
✅ 90-100 → "A"
✅ 80-89 → "B"
✅ 70-79 → "C"
✅ 60-69 → "D"
✅ Below 60 → "F" */

function getGrade(num) {
    if (num >= 90 && num <= 100) {
        return "Your grade is A"; // ✅ Use `return` instead of `console.log()`
    } else if (num >= 80 && num <= 89) {
        return "Your grade is B";
    } else if (num >= 70 && num <= 79) {
        return "Your grade is C";
    } else if (num >= 60 && num <= 69) {
        return "Your grade is D";
    } else {
        return "Your grade is F";
    }
}

console.log(getGrade(92)); // "A"
console.log(getGrade(75)); // "C"
console.log(getGrade(50)); // "F"