const bubbleSort = (arr) => {
  let temp;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length - 1; j++) {
      if (arr[j] > arr[i]) {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr;
};

const res = bubbleSort([2, 8, 5, 3, 9, 4, 1, 10]);
console.log(res);
