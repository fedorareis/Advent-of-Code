const fs = require("fs");

function nextChar(c) {
  return String.fromCharCode(c.charCodeAt(0) + 1);
}

function nodeComp(node, char) {
  const nodeVal = node == "S" ? "a" : node == "E" ? "z" : node;
  const charVal = char == "S" ? "a" : char == "E" ? "z" : char;
  return nodeVal.localeCompare(charVal) >= 0 || nextChar(nodeVal) == charVal;
}

let result = Infinity;
let input = [];
let start = [];
let end = [];
let adjMatrix = [];

try {
  input = fs
    .readFileSync("input.txt", "utf8")
    .split("\n")
    .map((line) => line.trim().split(""));
} catch (err) {
  console.error(err);
}

const nodes = input.length * input[0].length;
const rowLen = input[0].length;
const colLen = input.length;

nodeIdx = 0;
input.forEach((row, y) => {
  row.forEach((node, x) => {
    let temp = Array(nodes).fill(0);
    let nodeVal = node;
    if (node == "S" || node == "a") {
      nodeVal = "a";
      start.push(nodeIdx);
    }
    if (node == "E") {
      nodeVal = "z";
      end = nodeIdx;
    }
    if (y > 0 && nodeComp(nodeVal, input[y - 1][x])) {
      temp[nodeIdx - rowLen] = 1;
    }
    if (y < colLen - 1 && nodeComp(nodeVal, input[y + 1][x])) {
      temp[nodeIdx + rowLen] = 1;
    }
    if (x > 0 && nodeComp(nodeVal, input[y][x - 1])) {
      temp[nodeIdx - 1] = 1;
    }
    if (x < rowLen - 1 && nodeComp(nodeVal, input[y][x + 1])) {
      temp[nodeIdx + 1] = 1;
    }
    adjMatrix.push(temp);
    nodeIdx++;
  });
});

// Dijkstra's algorithm implementation from https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
// A Javascript program for Dijkstra's single
// source shortest path algorithm.
// The program is for adjacency matrix
// representation of the graph
let V = nodes;

// A utility function to find the
// vertex with minimum distance
// value, from the set of vertices
// not yet included in shortest
// path tree
function minDistance(dist, sptSet) {
  // Initialize min value
  let min = Number.MAX_VALUE;
  let min_index = -1;

  for (let v = 0; v < V; v++) {
    if (sptSet[v] == false && dist[v] <= min) {
      min = dist[v];
      min_index = v;
    }
  }
  return min_index;
}

// Function that implements Dijkstra's
// single source shortest path algorithm
// for a graph represented using adjacency
// matrix representation
function dijkstra(graph, src) {
  let dist = new Array(V);
  let sptSet = new Array(V);

  // Initialize all distances as
  // INFINITE and stpSet[] as false
  for (let i = 0; i < V; i++) {
    dist[i] = Number.MAX_VALUE;
    sptSet[i] = false;
  }

  // Distance of source vertex
  // from itself is always 0
  dist[src] = 0;

  // Find shortest path for all vertices
  for (let count = 0; count < V - 1; count++) {
    // Pick the minimum distance vertex
    // from the set of vertices not yet
    // processed. u is always equal to
    // src in first iteration.
    let u = minDistance(dist, sptSet);

    // Mark the picked vertex as processed
    sptSet[u] = true;

    // Update dist value of the adjacent
    // vertices of the picked vertex.
    for (let v = 0; v < V; v++) {
      // Update dist[v] only if is not in
      // sptSet, there is an edge from u
      // to v, and total weight of path
      // from src to v through u is smaller
      // than current value of dist[v]
      if (
        !sptSet[v] &&
        graph[u][v] != 0 &&
        dist[u] != Number.MAX_VALUE &&
        dist[u] + graph[u][v] < dist[v]
      ) {
        dist[v] = dist[u] + graph[u][v];
      }
    }
  }

  // return distance to the end
  return dist[end];
}

// This code is contributed by rag2127

start.forEach((val) => {
  const temp = dijkstra(adjMatrix, val);
  result = temp < result ? temp : result;
});

console.log(result);
