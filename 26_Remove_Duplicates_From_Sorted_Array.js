/**

 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var uniqueNums = [...new Set(nums)];
    nums.length = 0;
    nums.push(...uniqueNums);
    return nums.length
};
