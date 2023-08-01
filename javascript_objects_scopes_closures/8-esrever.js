#!/usr/bin/node

exports.esrever = function (putThatThangDownFlipItAndReverseIt) {
  const desever = [];
  for (let i = putThatThangDownFlipItAndReverseIt.length - 1; i >= 0; i--) {
    desever.push(putThatThangDownFlipItAndReverseIt[i]);
  }
  return desever;
};
