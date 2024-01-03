#!/usr/bin/node
// A script that reads and prints contents of a file

const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', (err, contents) => {
  if (err) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
