function checkPasswordStrength(password) {
  const strong = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
  return strong.test(password) ? "Strong" : "Weak";
}

console.log(checkPasswordStrength("P@ssword123"));
