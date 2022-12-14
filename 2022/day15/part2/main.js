const fs = require("fs");

let result = 0;

try {
  input = fs
    .readFileSync("input.txt", "utf8")
    .split("\n")
    .map((line) => line.trim());
} catch (err) {
  console.error(err);
}

console.log(result);
