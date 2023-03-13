const fs = require("fs");

const searchY = 2000000;

function printMap(map, yOffset = 0) {
  map.forEach((row, idx) => {
    console.log(`${idx - yOffset}\t${row.join("")}`);
  });
}

function generatePairs(input) {
  res = {
    minX: 0,
    maxX: 0,
    maxY: 0,
    maxDistance: 0,
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
    const pair = [sensor, beacon];
    pair.forEach((coord) => {
      if (coord[0] < res.minX) {
        res.minX = coord[0];
      }
      if (coord[0] > res.maxX) {
        res.maxX = coord[0];
      }
      if (coord[1] > res.maxY) {
        res.maxY = coord[1];
      }
    });
    if (distance > res.maxDistance) {
      res.maxDistance = distance;
    }
    res.pairs.push({
      sensor: sensor,
      beacon: beacon,
      distance: distance,
    });
  });

  return [res.minX, res.maxX, res.maxY, res.maxDistance, res.pairs];
}

function fillLine(xOffset, pair, line) {
  if (pair.sensor[1] == searchY) {
    line[pair.sensor[0] + xOffset] = "S";
  }
  if (pair.beacon[1] == searchY) {
    line[pair.beacon[0] + xOffset] = "B";
  }
  for (let y = -pair.distance; y <= pair.distance; y++) {
    if (y + pair.sensor[1] == searchY) {
      for (
        let x = -Math.abs(Math.abs(y) - pair.distance);
        x <= Math.abs(Math.abs(y) - pair.distance);
        x++
      ) {
        if (line[x + xOffset + pair.sensor[0]] == ".") {
          line[x + xOffset + pair.sensor[0]] = "#";
        }
      }
    }
  }
}

let result = 0;

try {
  input = fs
    .readFileSync("input.txt", "utf8")
    .split("\n")
    .map((line) => line.trim());
} catch (err) {
  console.error(err);
}

let [minX, maxX, maxY, maxDistance, pairs] = generatePairs(input);
// shifts any negative vlaues to positive and
// adds a buffer on the left for area covered by sensors
const xOffset = -minX + maxDistance;

let searchLine = Array(maxX + xOffset + maxDistance).fill(".");

pairs.forEach((pair) => {
  fillLine(xOffset, pair, searchLine);
});

searchLine.forEach((val) => {
  if (val != "." && val != "B") {
    result++;
  }
});

console.log(result);
