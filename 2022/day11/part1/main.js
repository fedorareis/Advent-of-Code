const fs = require("fs");

function processInput(input) {
  const ops = {
    "+": (a, b) => a + b,
    "*": (a, b) => a * b,
  };
  let res = [];
  let monkey = {};
  for (let idx = 0; idx < input.length; idx += 7) {
    monkey["total"] = 0;
    monkey["monkey"] = parseInt(input[idx].split("Monkey ")[1].split(":")[0]);
    monkey["items"] = input[idx + 1]
      .split("Starting items: ")[1]
      .split(",")
      .map((val) => parseInt(val.trim()));
    let temp = input[idx + 2].split("Operation: new = ")[1];
    monkey["operation"] = (val) => {
      return eval(temp.replaceAll("old", val));
    };
    const testVal = parseInt(input[idx + 3].split("Test: divisible by ")[1]);
    monkey["testVal"] = testVal;
    const ifTrue = parseInt(
      input[idx + 4].split("If true: throw to monkey ")[1]
    );
    const ifFalse = parseInt(
      input[idx + 5].split("If false: throw to monkey ")[1]
    );

    monkey["test"] = (val) => {
      return val % testVal == 0 ? ifTrue : ifFalse;
    };
    res.push(monkey);
    monkey = {};
  }
  return res;
}

let result = 0;
let rounds = 1;
let monkeys = [];

try {
  const data = fs
    .readFileSync("input.txt", "utf8")
    .split("\n")
    .map((line) => line.trim());
  monkeys = processInput(data);
} catch (err) {
  console.error(err);
}
const lcm = monkeys.reduce((a, b) => a * b.testVal, monkeys[0].testVal);

while (rounds <= 20) {
  monkeys.forEach((monkey) => {
    while (monkey.items.length) {
      monkey.total++;
      let item = monkey.items.shift();
      item = monkey.operation(item);
      item = Math.floor(item / 3);
      let pass = monkey.test(item);
      monkeys[pass].items.push(item);
    }
  });
  rounds++;
}

monkeys.sort((a, b) => b.total - a.total);
result = monkeys[0]["total"] * monkeys[1]["total"];

console.log(result);
