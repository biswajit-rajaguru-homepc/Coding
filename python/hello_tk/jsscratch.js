// nums = [1, 2, 3, 4]

// const runningSum = function (nums) {
//     running_Sum = []
//     sum = 0
//     for(const num of nums) {
//         sum += num
//         running_Sum.push(sum)
//     }
//     return running_Sum
// }

// console.log(runningSum(nums))

letters = {}
alphabet = Array.from(Array(26).keys()).map((c) => String.fromCharCode(c + 97))
alphabet.forEach((letter) => letters[letter] = 0)
console.log(letters)