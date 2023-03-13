const fs = require("fs");

let result = 0;

try {
  input = fs
    .readFileSync("ex.txt", "utf8")
    .split("\n")
    .map((line) =>
      line
        .trim()
        .split(",")
        .map((val) => parseInt(val))
    );
} catch (err) {
  console.error(err);
}

let minX = Infinity;
let minY = Infinity;
let minZ = Infinity;
let maxX = 0;
let maxY = 0;
let maxZ = 0;

input.forEach((cube) => {
  if (cube[0] < minX) {
    minX = cube[0];
  }
  if (cube[1] < minY) {
    minY = cube[1];
  }
  if (cube[2] < minZ) {
    minZ = cube[2];
  }

  if (cube[0] > maxX) {
    maxX = cube[0];
  }
  if (cube[1] > maxY) {
    maxY = cube[1];
  }
  if (cube[2] > maxZ) {
    maxZ = cube[2];
  }
});

let map = [];
for (let x = 0; x <= maxX - minX; x++) {
  col = [];
  for (let y = 0; y <= maxY - minY; y++) {
    depth = [];
    for (let z = 0; z <= maxZ - minZ; z++) {
      depth.push(".");
    }
    col.push(depth);
  }
  map.push(col);
}

input.forEach((drop) => {
  map[drop[0] - minX][drop[1] - minY][drop[2] - minZ] = "#";
});

console.log(map);

console.log(result);
