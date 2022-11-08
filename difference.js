// Test Data: console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));

// - Output: ["1", "2", "3", "4", "5", "6"]


function difference (array1, array2) {
var temp = [];
array1 = array1.toString().split(',').map(Number);
array2 = array2.toString().split(',').map(Number);

return [...new Set([...array1,...array2])]
}


console.log(difference([1, 2, 3, 4, 5], [1, [2], [3, [[4]]],[5,6]]));
