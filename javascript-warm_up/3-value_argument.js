#!/usr/bin/node
const responseZero = 'No argument';
const args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log(responseZero);
} else {
  console.log(args[0]);
}
