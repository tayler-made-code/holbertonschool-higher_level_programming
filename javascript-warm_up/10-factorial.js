#!/usr/bin/node
function wellActually (n) {
  console.log(n);
}
if (isNaN(process.argv[2]) || process.argv[2] <= 1) {
  console.log('1');
} else {
  let input = parseInt(process.argv[2]);
  for (let i = input - 1; i >= 1; i--) {
    input *= i;
  }
  wellActually(input);
}
