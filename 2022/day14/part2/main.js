const fs = require("fs");

let result = 0;
let input = "";
let map = [];

try {
  input = fs
    .readFileSync("input.txt", "utf8")
    .split("\n")
    .map((line) => line.trim());
} catch (err) {
  console.error(err);
}

smallestX = Infinity;

largeX = 0;
largeY = 0;

input.forEach((rock) => {
  const rockSides = rock.split(" -> ");
  rockSides.forEach((point) => {
    const [x, y] = point.split(",").map((val) => parseInt(val));
    if (x > largeX) {
      largeX = x;
    }
    if (y > largeY) {
      largeY = y;
    }
    if (x < smallestX) {
      smallestX = x;
    }
  });
});
for (let i = 0; i <= largeY + 1; i++) {
  map.push(Array(largeX * 2 + 1).fill("."));
}
map.push(Array(largeX * 2 + 1).fill("#"));

input.forEach((rock) => {
  const rockSides = rock.split(" -> ");
  let preX;
  let preY;
  rockSides.forEach((point, idx) => {
    const [x, y] = point.split(",").map((val) => parseInt(val));
    if (idx != 0) {
      if (preX < x) {
        while (preX <= x) {
          map[y][preX] = "#";
          preX++;
        }
      } else {
        while (preX >= x) {
          map[y][preX] = "#";
          preX--;
        }
      }

      if (preY < y) {
        while (preY <= y) {
          map[preY][x] = "#";
          preY++;
        }
      } else {
        while (preY >= y) {
          map[preY][x] = "#";
          preY--;
        }
      }
    }
    preX = x;
    preY = y;
  });
});
map[0][500] = "+";

let fallX = 500;
let fallY = 0;

while (fallY < map.length - 1 && fallX > 0 && fallY < map[0].length - 1) {
  if (map[fallY + 1][fallX] == ".") {
    fallY++;
  } else if (fallX - 1 < 0) {
    map[fallY][fallX] = "o";
    fallX = 500;
    fallY = 0;
  } else if (map[fallY + 1][fallX - 1] == ".") {
    fallY++;
    fallX--;
  } else if (fallX + 1 == map[0].length) {
    map[fallY][fallX] = "o";
    fallX = 500;
    fallY = 0;
  } else if (map[fallY + 1][fallX + 1] == ".") {
    fallY++;
    fallX++;
  } else if (fallX == 500 && fallY == 0) {
    result++;
    map[fallY][fallX] = "o";
    break;
  } else {
    map[fallY][fallX] = "o";
    result++;
    fallX = 500;
    fallY = 0;
  }
}

console.log(result);
