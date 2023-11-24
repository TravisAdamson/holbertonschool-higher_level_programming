#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('0');
} else {
  let nextHigh = args[0];
  let theHigh = 0;
  if (args[1] < nextHigh) {
    theHigh = nextHigh;
    nextHigh = args[1];
  } else {
    theHigh = args[1];
  }
  for (let i = 2; i < args.length; i++) {
    if (args[i] === theHigh) {
      nextHigh = args[i];
    } else if (args[i] > theHigh) {
      nextHigh = theHigh;
      theHigh = args[i];
    } else if (args[i] > nextHigh && args[i] < theHigh) {
      nextHigh = args[i];
    }
  }
  console.log(nextHigh);
}
