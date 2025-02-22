// 1. Start with Start with an array called inputtable. The array should have numbers between 1 and 10.
let inputtable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


// 2. Use inputtable from step 1 to create the following: -
// a. Set of multiples of 5 between 1 and 51. Name it fiveTable, print the contents to the console
fiveTable = inputtable.map((num) => {return num * 5})
console.log("fiveTable: " + fiveTable)
// b. Set of multiples of 13 between 1 and 131. Name it thirteenTable, print the contents to the console
thirteenTable = inputtable.map((num) => {return num * 13})
console.log("thirteenTable: " + thirteenTable)
// c. Set of squares of the numbers in inputtable. Name it squaresTable, print the contents to the console
squaresTable = inputtable.map((num) => {return num**2})
console.log("squaresTable: " + squaresTable)


// 3. Get (and then print) the odd multiples of 5 between 1 and 100. 5, 15, ...
oddFiveTable = fiveTable.filter((num) => {if (num % 2 !== 0){return true}})
console.log("oddFiveTable: " + oddFiveTable)


// 4. Get (and then print) the sum of even multiples of 7 between 1 and 100.
// Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from
multiplesOf7 = Array.from({ length : 15 }, (_, i) => i * 7)
evenMultiplesOf7 = multiplesOf7.filter((num) => {if (num % 2 === 0 ) return true})
sumOfMultiplesOf7 = evenMultiplesOf7.reduce((sum, val) => sum + val, 0)
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

hasRadiusCurry = currying(5)

// a. Use r = 5 and h = 10 to call your curried function.
part5a = hasRadiusCurry(10)
console.log("r = 5 & h = 10: " + part5a)

//b. Reuse the function from part ‘a’ but use h = 17
part5b = hasRadiusCurry(17)
console.log("r = 5 & h = 17: " + part5b)

//c. Reuse the function from part ‘a’ but use h = 11
part5c = hasRadiusCurry(11)
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

topics = trMaker(thMaker("First") + thMaker("Last") + thMaker("Age"))
entry1 = trMaker(thMaker("Joe") + thMaker("Biden") + thMaker("Really Old"))
entry1 = trMaker(thMaker("Mitch") + thMaker("McConnell") + thMaker("Retirement Age"))

coolHTMLTable = tableMaker(topics + entry1 + entry1)
console.log(coolHTMLTable)

// 7. Do the ‘generic’ version of questions 3 and 4, meaning the target
// multiple must not be hard coded; hint: we studied closures and currying. This means you
// should be able to use the same code to handle multiple scenarios, for example: first odd
// multiples of 11 and then even multiples of 3 (still in the range 1 to 100). Your code
//should allow the grader to combine a chosen multiple along with the choice of odd / even
// without modifying your code. 

coolGenericFunction = function(multiple){
    const multipleTable = Array.from({ length : 100 / Math.ceil(multiple) }, (_, i) => i * multiple)
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

        return divisibleTable
    }
}

// FOR GRADERS: Change the value of multiple and even variable to generate various tables
const multiple = 5
const isEven = true

// Test Code
multipleTable = coolGenericFunction(multiple)
evenOrOddMultipleTable = multiple5Table(isEven) 
console.log(evenOrOddMultipleTable)