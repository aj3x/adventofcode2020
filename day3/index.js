const input = require("./input");

const arr = input.split("\n");
const rowLength = arr[0].length;
function move(pos, x, y) {
  return [pos[0] + y, (pos[1] + x) % rowLength];
}

function sumPath(x, y) {
  let cur = [0, 0];
  const dict = {};
  while (cur[0] < arr.length) {
    const char = arr[cur[0]][cur[1]];
    if (!dict[char]) {
      dict[char] = 0;
    }
    dict[char]++;
    cur = move(cur, x, y);
  }
  return dict['#'];
}
let moves = [
[1,1],
[3,1],
[5,1],
[7,1],
[1,2],
]

const rval = moves.reduce((product, [x,y]) => {
  const z = sumPath(x,y);
  console.log(z);
  return product * sumPath(x,y);
}, 1);
console.log(rval);