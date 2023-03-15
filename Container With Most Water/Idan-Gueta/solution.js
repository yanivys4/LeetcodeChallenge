/**
 * @param {number[]} height
 * @return {number}
 */


var maxArea = function(height) {
      let leftPivotIndex = 0;
  let rightPivotIndex = height.length - 1;
  let maxArea = 0;
  while (leftPivotIndex < rightPivotIndex) {
    let area =
      (rightPivotIndex - leftPivotIndex) *
      Math.min(height[leftPivotIndex], height[rightPivotIndex]);
    maxArea = Math.max(area, maxArea);

    if (height[leftPivotIndex] > height[rightPivotIndex]) {
      rightPivotIndex--;
    } else {
      leftPivotIndex++;
    }
  }
  return maxArea;
};