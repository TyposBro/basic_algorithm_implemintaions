const insertionSort = (arr) => {
  for (let i = 1; i < arr.length; i++) {
    const element = arr[i];
    let j = i - 1;
    while (j >= 0 && element < arr[j]) {
      arr[j + 1] = arr[j];
      j -= 1;
    }
    arr[j + 1] = element;
  }
  return arr;
};

const foo = insertionSort([2, 8, 5, 3, 9, 4, 1, 10]);
console.log(foo);
