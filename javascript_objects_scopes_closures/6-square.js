#!/usr/bin/node

const FirstSquare = require('./5-square.js');

module.exports = class Square extends FirstSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let thisLine = '';
        for (let j = 0; j < this.width; j++) {
          thisLine += c;
        }
        console.log(thisLine);
      }
    }
  }
};
