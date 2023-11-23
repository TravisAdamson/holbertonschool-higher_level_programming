#!/usr/bin/node
const args = process.argv.slice(2);
const zeroInt = parseInt(args[0]);
if (isNaN(zeroInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + zeroInt);
}
