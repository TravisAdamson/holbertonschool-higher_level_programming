#!/usr/bin/node

const fileSource = require('fs');
const firstFile = fileSource.readFileSync(process.argv[2], 'utf8');
const secondFile = fileSource.readFileSync(process.argv[3], 'utf8');
fileSource.writeFileSync(process.argv[4], firstFile + secondFile);
