const input = [{ a: 1 }, { b: 2 }, { c: 3 }];
const output = {};
for (const item of input) {

  const key = Object.keys(item)[0]; 
  const value = item[key];
  
  output[key] = value;
}

console.log(output);
