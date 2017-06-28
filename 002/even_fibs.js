var total = 0;
var f = [1, 1];

while (f[0] < 4e6) {
  if (f[0] % 2 === 0) {
    total += f[0];
  }
  f = [f[1], f[0] + f[1]];
}
console.log(total);