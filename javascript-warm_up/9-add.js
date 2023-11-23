#!/usr/bin/node

function add (a, b) {
  const args = process.argv.slice(2);
  const zeroInt = parseInt(args[0]);
  const oneInt = parseInt(args[1]);
  if (isNaN(zeroInt) || (isNaN(oneInt))) {
    console.log('NaN');
  } else {
    const intResult = zeroInt + oneInt;
    console.log(intResult);
  }
}
