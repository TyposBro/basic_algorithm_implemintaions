const binarySearch = (list, item) => {
  let location = 0;
  let l = 0;
  let r = list.length - 1;
  while (l < r) {
    let m = Math.floor((l + r) / 2);
    if (item > list[m]) {
      l = m + 1;
    } else {
      r = m;
    }
  }
  if ((item = list[l])) {
    location = l;
  } else {
    location = 0;
  }
  return location;
};

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 9));
