#!/usr/bin/node

// To include the File System module, use the require() method
const fs = require('fs');
const filePath = process.argv[2];
const textToAdd = process.argv[3];

fs.appendFile(filePath, textToAdd, (err) => {
  if (err) {
    console.log(err);
  }
});
