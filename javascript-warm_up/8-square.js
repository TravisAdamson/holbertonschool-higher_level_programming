#!/usr/bin/node
const args = process.argv.slice(2);
const zeroInt = parseInt(args[0]);
if (isNaN(zeroInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < zeroInt; i++) {
    let thisLine = '';
    for (let j = 0; j < zeroInt; j++) {
      thisLine += 'X';
    }
    console.log(thisLine);
  }
}
