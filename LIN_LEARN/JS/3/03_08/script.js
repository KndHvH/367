var pens;
pens = ["red", "blue", "green", "orange"];

console.log("Before: ", pens);

// PROPERTIES:
// Get a property of an object by name:
console.log("Array length: ", pens.length);

// METHODS:
// Reverse the array:
pens.reverse();
console.log(pens)

// Remove the first value of the array:
pens.shift();
console.log(pens)

// Add comma-separated list of values to the front of the array:
pens.unshift("purple", "black");
console.log(pens)

// Remove the last value of the array:
pens.pop();
console.log(pens)

// Add comma-separated list of values to the end of the array:
pens.push("pink", "prussian blue");
console.log(pens)

// Find the specified position (pos) and remove n number of items from the array. Arguments: pens.splice(pos,n):
pens.splice(3, 2) // Starts at the second item and removes two items.
console.log(pens)

console.log("After: ", pens);

// Create a copy of an array. Typically assigned to a new variable:
var newPens = pens.slice();
console.log("New pens: ", newPens);


// Return the first element that matches the search parameter after the specified index position. Defaults to index position 0. Arguments: pens.indexOf(search, index):
var result = pens.indexOf("orange", 1);
console.log("The search result index is: ", result);

var result = pens.indexOf("green");
console.log("The search result index is: ", result);

// Return the items in an array as a comma separated string. The separator argument can be used to change the comma to something else. Arguments: pens.join(separator):
var arrayString = pens.join(" ");
console.log("String from array: ", arrayString);

// MDN documentation for Array:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array


// Before:  (4) ['red', 'blue', 'green', 'orange']
// script.js:8 Array length:  4
// script.js:13 (4) ['orange', 'green', 'blue', 'red']
// script.js:17 (3) ['green', 'blue', 'red']
// script.js:21 (5) ['purple', 'black', 'green', 'blue', 'red']
// script.js:25 (4) ['purple', 'black', 'green', 'blue']
// script.js:29 (6) ['purple', 'black', 'green', 'blue', 'pink', 'prussian blue']
// script.js:33 (4) ['purple', 'black', 'green', 'prussian blue']
// script.js:35 After:  (4) ['purple', 'black', 'green', 'prussian blue']
// script.js:39 New pens:  (4) ['purple', 'black', 'green', 'prussian blue']
// script.js:44 The search result index is:  -1
// script.js:47 The search result index is:  2
// script.js:51 String from array:  purple,black,green,prussian blue