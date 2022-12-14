const fs = require("fs");

function compare(left, right, firstOnly) {
  // console.log(left);
  // console.log(right);
  if (left.length > right.length && !firstOnly) {
    // console.log(left);
    // console.log(right);
    console.log("length mismatch");
    return false;
  }
  for (
    let idx = 0;
    (!firstOnly && idx < left.length) || (firstOnly && idx < 1);
    idx++
  ) {
    if (Array.isArray(left[idx]) && Array.isArray(right[idx])) {
      if (!compare(left[idx], right[idx], false)) {
        // console.error(left);
        // console.error(right);
        console.error("fail 2 arrays");
        return false;
      }
    } else if (Array.isArray(left[idx]) && !Array.isArray(right[idx])) {
      if (!compare(left[idx], [right[idx]], true)) {
        // console.error(left);
        // console.error(right);
        console.error("fail array - int");
        return false;
      }
    } else if (!Array.isArray(left[idx]) && Array.isArray(right[idx])) {
      if (!compare([left[idx]], right[idx], false)) {
        // console.error(left);
        // console.error(right);
        console.error("fail int - array");
        return false;
      }
    } else {
      if (left[idx] > right[idx]) {
        // console.error(left);
        // console.error(right);
        console.error(`${left[idx]} > ${right[idx]}`);
        return false;
      }
    }
  }
  return true;
}

let result = 0;
let input = "";

try {
  input = fs
    .readFileSync("ex.txt", "utf8")
    .split("\n")
    .filter((line) => line.trim() != "")
    .map((line) => JSON.parse(line.trim()));
} catch (err) {
  console.error(err);
}

// console.log(compare([[1], [2, 3, 4]], [[1], 4], false));

for (let i = 0; i < input.length; i += 2) {
  const left = input[i];
  const right = input[i + 1];
  // console.log(i / 2 + 1);
  if (compare(left, right, false)) {
    console.log(i / 2 + 1);
    result += i / 2 + 1;
  }
}

console.log(result);
