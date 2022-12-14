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
  map.push(Array(largeX + 1).fill("."));
}

const printMap = () => {
  map.forEach((row) => {
    let x = smallestX - 2 > 0 ? smallestX - 2 : smallestX > 0 ? smallestX : 0;
    console.log(row.slice(x).join(""));
  });
};

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
  if (fallY + 1 == map.length) {
    break;
  }
  if (map[fallY + 1][fallX] == ".") {
    fallY++;
  } else if (fallX - 1 < 0) {
    break;
  } else if (map[fallY + 1][fallX - 1] == ".") {
    fallY++;
    fallX--;
  } else if (fallX + 1 == map[0].length) {
    break;
  } else if (map[fallY + 1][fallX + 1] == ".") {
    fallY++;
    fallX++;
  } else {
    map[fallY][fallX] = "o";
    result++;
    fallX = 500;
    fallY = 0;
  }
}

console.log(result);
