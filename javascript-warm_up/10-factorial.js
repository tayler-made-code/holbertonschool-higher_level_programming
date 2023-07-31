#!/usr/bin/node
function wellActually (n) {
    console.log(n);
  }

  if (isNaN(process.argv[2]) || process.argv[2] === 0 || process.argv[2] === 1) {
    console.log('1');
  } else {
    let n = parseInt(process.argv[2]);
    for (let i = n - 1; i >= 1; i--) {
        n *= i;
        }
    wellActually(n);
    }

