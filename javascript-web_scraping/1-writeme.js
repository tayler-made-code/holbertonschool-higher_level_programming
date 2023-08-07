#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const textToAdd = process.argv[3];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);

    if (textToAdd) {
      fs.appendFile(filePath, textToAdd, (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  }
});
