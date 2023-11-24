#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('0');
} else {
  let nextHigh = parseInt(args[0]);
  let theHigh = parseInt(args[1]);
  if (theHigh < nextHigh) {
    theHigh = nextHigh;
    nextHigh = parseInt(args[1]);
  }
  for (let i = 2; i < args.length; i++) {
    const newVal = parseInt(args[i]);
    if (newVal === theHigh) {
      nextHigh = newVal;
    } else if (newVal > theHigh) {
      nextHigh = theHigh;
      theHigh = newVal;
    } else if (newVal > nextHigh && newVal < theHigh) {
      nextHigh = newVal;
    }
  }
  console.log(nextHigh);
}
