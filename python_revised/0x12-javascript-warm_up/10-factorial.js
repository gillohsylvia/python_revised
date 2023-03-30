#!/usr/bin/node
const a = Math.floor(Number(process.argv[2]));

function factorial(a) {
  if (Number.isInteger(a)) {
          if (a === 0) {
                  return 1;
          } else {
                  return a * factorial(a -1);
          }
  }else {
          return 1;
  }
}
console.log(factorial(a));
