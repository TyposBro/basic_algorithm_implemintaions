function mergeSort(arr: number[]): number[] {
  if (arr.length < 2) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
}

function merge(left: number[], right: number[]): number[] {
  const arr: number[] = [];
  let l = 0;
  let r = 0;

  while (l < left.length && r < right.length) {
    if (left[l] < right[r]) {
      arr.push(left[l]);
      l++;
    } else {
      arr.push(right[r]);
      r++;
    }
  }

  return arr.concat(left.slice(l)).concat(right.slice(r));
}

const res = mergeSort([2, 8, 5, 3, 9, 4, 1, 10]);
console.log(res);
