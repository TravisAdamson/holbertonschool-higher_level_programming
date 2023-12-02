#!/usr/bin/node
const request = require('request');
const thisUrl = 'https://swapi-api.hbtn.io/api/films/' + ProcessingInstruction.argv[2];
request(thisUrl, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
