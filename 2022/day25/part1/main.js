const fs = require("fs");

let result = 0;
let map = {
  2: 2,
  1: 1,
  0: 0,
  "-": -1,
  "=": -2,
};

function toSNAFU(val) {}

try {
  input = fs
    .readFileSync("input.txt", "utf8")
    .split("\n")
    .map((line) => line.trim());
} catch (err) {
  console.error(err);
}

input.forEach((val) => {
  const len = val.length;
  let snafu = 0;
  for (let i = 0; i < len; i++) {
    const pow = 5 ** (len - (i + 1));
    snafu += pow * map[val.charAt(i)];
  }
  console.log(val, snafu);
  result += snafu;
});

console.log(result);
