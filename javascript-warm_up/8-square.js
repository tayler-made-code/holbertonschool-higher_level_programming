#!/usr/bin/node

const buildingMaterial = 'X';

if (isNaN(process.argv[2])) {
  console.log('Missing size');
  process.exit();
}

for (let i = 0; i < process.argv[2]; i++) {
  console.log(buildingMaterial.repeat(process.argv[2]));
}
