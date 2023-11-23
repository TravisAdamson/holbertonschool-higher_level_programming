#!/usr/bin/node
const responseZero = 'No argument';
const responseOne = 'Argument found';
const responseMore = 'Arguments found';
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log(responseZero);
} else if (args.length === 1) {
  console.log(responseOne);
} else {
  console.log(responseMore);
}
