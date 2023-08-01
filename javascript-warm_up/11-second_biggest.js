#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const totalArgs = process.argv.length;
  let currentHighest = parseInt(process.argv[2]);
  let secondHighest = parseInt(process.argv[3]);

  for (let iterate = 3; iterate < totalArgs; iterate++) {
    const compare = parseInt(process.argv[iterate]);
    if (currentHighest < compare) {
      secondHighest = currentHighest;
      currentHighest = compare;
    } else if (secondHighest < compare) {
      secondHighest = compare;
    }
  }
  console.log(secondHighest);
}
