#!/usr/bin/node

function nbOccurences (bigOlePileofSchtuff, disOne) {
  let disMany = 0;
  for (const element of bigOlePileofSchtuff) {
    if (element === disOne) {
      disMany++;
    }
  }
  return disMany;
}

exports.nbOccurences = nbOccurences;
