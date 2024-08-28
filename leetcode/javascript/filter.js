//Given an integer array arr and a filtering function fn, return a filtered array filteredArr.

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  const res = [];

  for (let i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      res.push(arr[i]);
    }
  }
  return res;
};
