function customMap(arr, callback) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(callback(arr[i], i, arr));
  }
  return result;
}

// Example usage:
const numbers = [1, 2, 3, 4];
const doubled = customMap(numbers, num => num * 2);
console.log(doubled); // Output: [2, 4, 6, 8]
