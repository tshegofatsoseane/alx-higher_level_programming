#!/usr/bin/node
// A script that displays the title of a Star Wars movie

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request({ url: url, json: true }, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(res.body.title);
  }
});
