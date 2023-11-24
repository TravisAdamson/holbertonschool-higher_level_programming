#!/usr/bin/node

const Square = require('./5-rectangle.js');

module.exports = class Square extends Square {
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
