/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    y = x
    y = y.toString();
    rev = y.split('')
    rev = rev.reverse()
    rev = rev.join('');
    return y === rev
};
