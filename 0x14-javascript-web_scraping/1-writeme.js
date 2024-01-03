#!/usr/bin/node
// A script that writes string to a given file

const fs = require('fs');
const filepath = process.argv[2];
const contents = process.argv[3];

fs.writeFile(filepath, contents, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
