#!/usr/bin/node

const theList = require('./100-data.js').list;
console.log(theList);
console.log(theList.map((item, index) => item * index));
