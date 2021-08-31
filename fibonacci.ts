function fibonacci(n: number) {
  let arr = [];
  let first = 0;
  let sec = 1;
  arr.push(first);
  arr.push(sec);
  if (n <= 0) {
    arr = [0];
  } else {
    while (arr.length <= n) {
      arr.push(arr[first] + arr[sec]);
      first++;
      sec++;
    }
  }
  return arr;
}
console.log(fibonacci(10));
