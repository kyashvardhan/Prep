function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

// Example usage:
const original = { a: 1, b: { c: 2 } };
const cloned = deepClone(original);
cloned.b.c = 99;
console.log("Original:", original); // b.c remains 2
console.log("Cloned:", cloned);     // b.c is 99
