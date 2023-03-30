#!/usr/bin/node
const args = process.argv.slice(2);
const num = args.map(Number);
const sorted = num.sort((a, b) => a - b);
if (sorted.length === 0) {
    console.log(0);
} else if (sorted.length === 1) {
    console.log(1);
} else {
    console.log(sorted[sorted.length - 2]);
}
