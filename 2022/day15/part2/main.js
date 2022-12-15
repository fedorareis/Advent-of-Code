const fs = require("fs");

const searchMax = 4000000;

function printMap(map, yOffset = 0) {
  map.forEach((row, idx) => {
    console.log(`${idx - yOffset}\t${row.join("")}`);
  });
}

function generatePairs(input) {
  res = {
    pairs: [],
  };

  const getCoord = (val) => {
    return val
      .split("x=")[1]
      .split(", y=")
      .map((coord) => parseInt(coord));
  };

  input.forEach((line) => {
    const [sensorInfo, beaconInfo] = line.split(": ");
    const sensor = getCoord(sensorInfo);
    const beacon = getCoord(beaconInfo);
    const distance =
      Math.abs(sensor[0] - beacon[0]) + Math.abs(sensor[1] - beacon[1]);
    res.pairs.push({
      sensor: sensor,
      beacon: beacon,
      distance: distance,
    });
  });

  return res.pairs;
}

function fillLine(searchY, pair, line) {
  if (
    pair.sensor[1] == searchY &&
    pair.sensor[0] >= 0 &&
    pair.sensor[0] <= searchMax
  ) {
    line[pair.sensor[0]] = "S";
  }
  if (
    pair.beacon[1] == searchY &&
    pair.beacon[0] >= 0 &&
    pair.beacon[0] <= searchMax
  ) {
    line[pair.beacon[0]] = "B";
  }
  if (Math.abs(pair.sensor[1] - searchY) <= pair.distance) {
    let y =
      pair.sensor[1] <= searchY
        ? searchY - pair.sensor[1]
        : pair.sensor[1] - searchY;
    let startX =
      -Math.abs(Math.abs(y) - pair.distance) + pair.sensor[0] >= 0
        ? -Math.abs(Math.abs(y) - pair.distance) + pair.sensor[0]
        : 0;
    let endX =
      Math.abs(Math.abs(y) - pair.distance) + pair.sensor[0] <= searchMax
        ? Math.abs(Math.abs(y) - pair.distance) + pair.sensor[0]
        : searchMax;
    for (let x = startX; x <= endX; x++) {
      if (line[x] == ".") {
        line[x] = "#";
      }
    }
  }
}

let result = 0;
let map = [];

try {
  input = fs
    .readFileSync("input.txt", "utf8")
    .split("\n")
    .map((line) => line.trim());
} catch (err) {
  console.error(err);
}

const pairs = generatePairs(input);

for (y = 0; y <= searchMax; y++) {
  let searchLine = Array(searchMax).fill(".");
  console.log(y);
  pairs.forEach((pair) => {
    fillLine(y, pair, searchLine);
  });
  let x = searchLine.indexOf(".");
  if (x != -1) {
    result = x * 4000000 + y;
    break;
  }
}

console.log(result);
