#!/usr/bin/node

const unsortedDict = require('./101-data.js').dict;
const sortedDict = {};
for (const key in unsortedDict) {
  if (sortedDict[unsortedDict[key]] === undefined) {
    sortedDict[unsortedDict[key]] = [key];
  } else {
    sortedDict[unsortedDict[key]].push(key);
  }
}
console.log(sortedDict);
