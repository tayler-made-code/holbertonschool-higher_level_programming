#!/usr/bin/node

// Create a node that reads HTML files and returns the content
const dialUp = require('request');
// argument[2] is the URL to request
const webSite = process.argv[2];

dialUp.get(webSite, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + response.statusCode);
});
