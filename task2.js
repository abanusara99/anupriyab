const input = { a: 1, b: 2, c: 3 };
const output = [];

for (const key in input) {
    const item = {};
    item[key] = input[key];
    output.push(item);
}

console.log(output);
