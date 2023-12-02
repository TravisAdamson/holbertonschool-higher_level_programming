#!/usr/bin/node
const fileSys = require('fs');
const thisRequest = require('request');
thisRequest(process.argv[2]).pipe(fileSys.createWriteStream(process.argv[3]));
