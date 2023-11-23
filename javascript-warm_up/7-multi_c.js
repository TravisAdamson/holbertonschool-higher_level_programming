#!/usr/bin/node
const args = process.argv.slice(2);
const zeroInt = parseInt(args[0]);
if (isNaN(zeroInt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < zeroInt; i++) {
    console.log('C is fun');
  }
}
