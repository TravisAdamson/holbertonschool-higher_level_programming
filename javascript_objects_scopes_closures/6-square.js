#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
