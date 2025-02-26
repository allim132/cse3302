// Alex Nguyen
// 1002097417
// 2/25/2025

// 1. Start with Start with an array called inputtable. The array should have numbers between 1 and 10.
let inputtable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


// 2. Use inputtable from step 1 to create the following: -
// a. Set of multiples of 5 between 1 and 51. Name it fiveTable, print the contents to the console
fiveTable = inputtable.map((num) => {return num * 5}) 
// PROGRAMMING COMMENT: Use of map and lambda. Multiply the inputtable by 5 to create the five table
console.log("fiveTable: " + fiveTable)

// b. Set of multiples of 13 between 1 and 131. Name it thirteenTable, print the contents to the console
thirteenTable = inputtable.map((num) => {return num * 13})
// PROGRAMMING COMMENT: Use of map and lambda. Same process as the fiveTable initialization but multiply by 13
console.log("thirteenTable: " + thirteenTable)

// c. Set of squares of the numbers in inputtable. Name it squaresTable, print the contents to the console
squaresTable = inputtable.map((num) => {return num**2})
// PROGRAMMING COMMENT: Same as others, use of the very cool exponent operator instead of num * num
console.log("squaresTable: " + squaresTable)


// 3. Get (and then print) the odd multiples of 5 between 1 and 100. 5, 15, ...
oddFiveTable = fiveTable.filter((num) => {if (num % 2 !== 0) return true})
// PROGRAMMING COMMENT: Use of filter which passes a lambda which evaluates true if not even. 
// PROGRAMMING COMMENT: I assume that no return is logically the same as false, 
// because both values does not add to the array and gets "filterd" out.
console.log("oddFiveTable: " + oddFiveTable)


// 4. Get (and then print) the sum of even multiples of 7 between 1 and 100.
// Reference (For learning Array.from): https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from
multiplesOf7 = Array.from({ length : 15 }, (_, i) => i * 7)
// PROGRAMMING COMMENT: Use of reference to initialize the multiples of 7 between 1 and 100. 
// I got the number 15 from dividing 100 by 7 and rounding up. 
// I verified that this correctly yields the multiples of 7 by printing out the multiplesOf7 array.
evenMultiplesOf7 = multiplesOf7.filter((num) => {if (num % 2 === 0 ) return true})
// PROGRAMMING COMMENT: Same filter implementation as question 3.
sumOfMultiplesOf7 = evenMultiplesOf7.reduce((accumulator, val) => accumulator + val, 0)
// PROGRAMMING COMMENT: Very cool reduce function which requires a function (calculates sum) and a starting value (0).
console.log("sumOfMultiplesOf7: " + sumOfMultiplesOf7)

// 5. Use currying to rewrite the function below:
/*
function cylinder_volume(r, h){ 
    var volume = 3.14 * r * r * h; 
    return volume; 
}
*/
const currying = (r) => (h) => {
    return 3.14 * r * r * h
} 
// PROGRAMMING COMMENT: Very cool name. It utilizes currying referenced by the "So You Want to..." series.
hasRadiusCurry = currying(5)
// PROGRAMMING COMMENT: Binding the value of 5 for the radius.

// a. Use r = 5 and h = 10 to call your curried function.
part5a = hasRadiusCurry(10)
// PROGRAMMING COMMENT: Passing in 10 for the height.
console.log("r = 5 & h = 10: " + part5a)

//b. Reuse the function from part ‘a’ but use h = 17
part5b = hasRadiusCurry(17)
// PROGRAMMING COMMENT: Passing in 17 for the height.
console.log("r = 5 & h = 17: " + part5b)

//c. Reuse the function from part ‘a’ but use h = 11
part5c = hasRadiusCurry(11)
// PROGRAMMING COMMENT: Passing in 11 for the height.
console.log("r = 5 & h = 11: " + part5c)

// 6. Use the following code (insert it into your code) to take advantage of closures to wrap content with
// HTML tags, specifically show an HTML table consisting of a table row that has at least
// one table cell/element. You can use the console to output your results.
makeTag = function(beginTag, endTag){ 
    return function(textcontent){ 
       return beginTag +textcontent +endTag; 
    } 
}

tableMaker = makeTag("<table>\n", "</table>\n")
trMaker = makeTag("<tr>\n", "</tr>\n")
thMaker = makeTag("<th>", "</th>\n")
// PROGRAMMING COMMENT: Using the higher-order function makeTag to make various tags with appropriate new line characters

topics = trMaker(thMaker("First") + thMaker("Last") + thMaker("Age"))
entry1 = trMaker(thMaker("Joe") + thMaker("Biden") + thMaker("Really Old"))
entry1 = trMaker(thMaker("Mitch") + thMaker("McConnell") + thMaker("Retirement Age"))
// PROGRAMMING COMMENT: Creating the data for each 'tr' which probably means table row?

coolHTMLTable = tableMaker(topics + entry1 + entry1)
// PROGRAMMING COMMENT: Constructing the table by composing all the 'tr's together
console.log(coolHTMLTable)

// 7. Do the ‘generic’ version of questions 3 and 4, meaning the target
// multiple must not be hard coded; hint: we studied closures and currying. This means you
// should be able to use the same code to handle multiple scenarios, for example: first odd
// multiples of 11 and then even multiples of 3 (still in the range 1 to 100). Your code
// should allow the grader to combine a chosen multiple along with the choice of odd / even
// without modifying your code. 



const problem3GenericFunction = function(multiple){
    const multipleTable = Array.from({ length : 100 / Math.ceil(multiple) }, (_, i) => i * multiple)
    // PROGRAMMING COMMENT: I got this formula from the code in part 4. This is to create the create multiple 
    return function(even){
        const divisibleTable = multipleTable.filter((num) => {
            if (even) {
                if (num % 2 === 0 ) {
                    return true
                } else return false
            } else {
                if (num % 2 !== 0 ) {
                    return true
                } else return false
            }
        })
        // PROGRAMMING COMMENT: Modified version of the previous filter, with two cases for even or odd.

        return divisibleTable
    }
}

const problem4GenericFunction = (operation) => {
    return function(multiple, even){
        const array = problem3GenericFunction(multiple)(even)
        return array.reduce(operation)
    }
}
// --------------------------------------------------------------------------------------//
// FOR GRADERS: Change the value of multiple and even variable to generate various tables
const multiple = 5
const isEven = true
// --------------------------------------------------------------------------------------//

// Problem 3
multipleTable = problem3GenericFunction(multiple)
// PROGRAMMING COMMENT: Currying
evenOrOddMultipleTable = multipleTable(isEven) 
// PROGRAMMING COMMENT: Creation of array
console.log(evenOrOddMultipleTable)

// Problem 4

// FOR GRADERS: Change these to change parameters to change the output
const myCustomOperation = (accumulator, currentValue) => {
    return accumulator + currentValue
}
const coolerMultiple = 7
const coolerIsEven = false

const result = problem4GenericFunction(myCustomOperation)(coolerMultiple, coolerIsEven)
console.log(result)