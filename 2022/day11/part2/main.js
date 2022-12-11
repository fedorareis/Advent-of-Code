const generateData = (file) => {
  if (file == "ex") {
    return [
      {
        total: 0,
        monkey: 0,
        items: [79, 98],
        operation: (a) => {
          return a * 19;
        },
        testVal: 23,
        test: (a) => {
          return a % 23 == 0 ? 2 : 3;
        },
      },
      {
        total: 0,
        monkey: 1,
        items: [54, 65, 75, 74],
        operation: (a) => {
          return a + 6;
        },
        testVal: 19,
        test: (a) => {
          return a % 19 == 0 ? 2 : 0;
        },
      },
      {
        total: 0,
        monkey: 2,
        items: [79, 60, 97],
        operation: (a) => {
          return a * a;
        },
        testVal: 13,
        test: (a) => {
          return a % 13 == 0 ? 1 : 3;
        },
      },
      {
        total: 0,
        monkey: 3,
        items: [74],
        operation: (a) => {
          return a + 3;
        },
        testVal: 17,
        test: (a) => {
          return a % 17 == 0 ? 0 : 1;
        },
      },
    ];
  } else {
    return [
      {
        total: 0,
        monkey: 0,
        items: [85, 79, 63, 72],
        testVal: 2,
        operation: (a) => {
          return a * 17;
        },
        test: (a) => {
          return a % 2 == 0 ? 2 : 6;
        },
      },
      {
        total: 0,
        monkey: 1,
        items: [53, 94, 65, 81, 93, 73, 57, 92],
        testVal: 7,
        operation: (a) => {
          return a * a;
        },
        test: (a) => {
          return a % 7 == 0 ? 0 : 2;
        },
      },
      {
        total: 0,
        monkey: 2,
        items: [62, 63],
        testVal: 13,
        operation: (a) => {
          return a + 7;
        },
        test: (a) => {
          return a % 13 == 0 ? 7 : 6;
        },
      },
      {
        total: 0,
        monkey: 3,
        items: [57, 92, 56],
        testVal: 5,
        operation: (a) => {
          return a + 4;
        },
        test: (a) => {
          return a % 5 == 0 ? 4 : 5;
        },
      },
      {
        total: 0,
        monkey: 4,
        items: [67],
        testVal: 3,
        operation: (a) => {
          return a + 5;
        },
        test: (a) => {
          return a % 3 == 0 ? 1 : 5;
        },
      },
      {
        total: 0,
        monkey: 5,
        items: [85, 56, 66, 72, 57, 99],
        testVal: 19,
        operation: (a) => {
          return a + 6;
        },
        test: (a) => {
          return a % 19 == 0 ? 1 : 0;
        },
      },
      {
        total: 0,
        monkey: 6,
        items: [86, 65, 98, 97, 69],
        testVal: 11,
        operation: (a) => {
          return a * 13;
        },
        test: (a) => {
          return a % 11 == 0 ? 3 : 7;
        },
      },
      {
        total: 0,
        monkey: 7,
        items: [87, 68, 92, 66, 91, 50, 68],
        testVal: 17,
        operation: (a) => {
          return a + 2;
        },
        test: (a) => {
          return a % 17 == 0 ? 4 : 3;
        },
      },
    ];
  }
};

let result = 0;
let rounds = 1;
const monkeys = generateData("input");
const lcm = monkeys.reduce((a, b) => a * b.testVal, monkeys[0].testVal);

while (rounds <= 10000) {
  monkeys.forEach((monkey) => {
    while (monkey.items.length) {
      monkey.total++;
      let item = monkey.items.shift();
      item = monkey.operation(item);
      item = item % lcm;
      let pass = monkey.test(item);
      monkeys[pass].items.push(item);
    }
  });
  rounds++;
}

monkeys.sort((a, b) => b.total - a.total);
result = monkeys[0]["total"] * monkeys[1]["total"];

console.log(result);
