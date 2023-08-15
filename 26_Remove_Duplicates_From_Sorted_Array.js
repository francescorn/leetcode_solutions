/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    const uniqueNums = [...new Set(nums)];
    nums.splice([0, -1]);
    nums.push(...uniqueNums);
    return nums.length;
}
