#!/usr/bin/node

function factorial (a) {
  if (a < 0) {
    return 'Undefined';
  } else if (isNaN(a) || a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const args = process.argv.slice(2);
const zeroInt = parseInt(args[0]);
const resultVal = factorial(zeroInt);
console.log(resultVal.toString());
