const fs = require("fs");

let result = 0;

try {
  input = fs
    .readFileSync("input.txt", "utf8")
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

input.forEach((drop, idx) => {
  result += 6;
  for (let i = 0; i < idx; i++) {
    if (
      drop[0] == input[i][0] &&
      drop[1] == input[i][1] &&
      (drop[2] + 1 == input[i][2] || drop[2] - 1 == input[i][2])
    ) {
      result += -2;
    } else if (
      drop[1] == input[i][1] &&
      drop[2] == input[i][2] &&
      (drop[0] + 1 == input[i][0] || drop[0] - 1 == input[i][0])
    ) {
      result += -2;
    } else if (
      drop[0] == input[i][0] &&
      drop[2] == input[i][2] &&
      (drop[1] + 1 == input[i][1] || drop[1] - 1 == input[i][1])
    ) {
      result += -2;
    }
  }
});

console.log(result);
