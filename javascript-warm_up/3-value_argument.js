#!/usr/bin/node
const responseZero = 'No argument';
const args = process.argv.slice(2);
if (args[0] === null) {
  console.log(responseZero);
} else {
  console.log(args[0]);
}
