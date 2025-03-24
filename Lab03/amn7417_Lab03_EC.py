'''
Alex Nguyen | 1002097417 | amn7417

EXTRA CREDIT: 
Implemented exponent operator
'''

import os


'''
Approach:
0. Read Data and convert into string
1. Convert algebraic expression via Shunting-yard algorithm
    https://gist.github.com/ollybritton/3ecdd2b28344b0b25c547cbfcb807ddc
    https://www.martinbroadhurst.com/shunting-yard-algorithm-in-python
    https://tomekkorbak.com/2020/03/25/implementing-shunting-yard-parsing/
    https://www.andreinc.net/2010/10/05/converting-infix-to-rpn-shunting-yard-algorithm#:~:text=Reverse%20Polish%20Notation,-A%20+%20B&text=In%20order%20to%20parse%20and,%2C%20and%20one%20for%20output).
2. Use stack calculate value.
    2.a. If top of stack is an operation, pop the two numbers below it (handle edge cases) to run the operation
    2.b. Push result back onto the satck
3. If no more input, return a result iff there is only one element
    3.a. 
'''


# Step 0
# Sources: https://www.geeksforgeeks.org/python-os-open-method/
# https://www.geeksforgeeks.org/with-statement-in-python/
# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
# https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string
def input_file_to_string_list(inputFileName):
    stringList = []

    # "with" closes file afterwards automatically
    with open(inputFileName, "r") as file:
        stringList = file.readlines()
    
    # Remove excess left/right spaces
    stringList = map(lambda line: line.strip(), stringList)

    return list(stringList)


# Step 1

# Before using the RPN_converter, it is useful to tokenize the string so this handles multi-digit numbers
# Use of Shunting Yard algorithm which processes number, parenthesis, 
'''
RPN_converter
@ param
expression: A string in the format of an algebriac expression

Returns a tokenized list of the input but in RPN form
'''
def RPN_converter(expression):
    tokenized_line = tokenizer(expression)

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    output_queue = []
    operator_stack = []

    for token in tokenized_line:
        #print(f"token: {token}")
        if token.isdigit():
            output_queue.append(token)
        elif token in precedence:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence[token] <= precedence.get(operator_stack[-1], 0)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()  # Remove the '('

    while operator_stack:
        output_queue.append(operator_stack.pop())


    return output_queue


'''
Tokenizer
@ param
line: A string of character in algebriac form

Returns a tokenized list of the input
'''
def tokenizer(line):
    line = line.replace(" ", "")

    tokens = []

    i = 0
    tokenIndex = 0;
    while i < len(line):
        #print(f"i = {i}, tokenIndex = {tokenIndex}")
        #print(f"tokenizer char: {line[i]}")
        if line[i].isspace(): # space
            i += 1
        elif line[i] in '*/+-()%': # operation
            tokens.append(line[i])
            i += 1
            tokenIndex += 1
        else: # everything else
            number = ''
            while i < len(line) and line[i].isdigit():
                number += line[i]
                i += 1
            tokens.append(number)

    #print(f"tokens = {tokens}")
    return tokens

# Step 2
'''
compute_RPN
@param
RPN_expression: A list of tokens in the RPN format

Returns an int result. Does not have error handling
'''
def compute_RPN(RPN_expression):
    result = 0
    stack = []

    for token in RPN_expression:
        if token in '*/+-%': # If operation, run it
            secondValue = int(stack.pop())
            firstValue = int(stack.pop())
            result = doOperation(firstValue, secondValue, token)
            stack.append(result)
        else: # If number, add to the stack
            stack.append(token)

    if stack:
        return stack[0]  # Return the final result from the stack
    else:
        return 0  # Handle empty expression case

'''
doOperation
@ param
firstValue: Int
secondValue: Int
operator: String in '*/%+-'

Returns the result of the first and second value running the appropriate operation
'''
def doOperation(firstValue, secondValue, operator):
    if operator == '+':
        return firstValue + secondValue
    elif operator == '-':
        return firstValue - secondValue
    elif operator == '*':
        return firstValue * secondValue
    elif operator == '/':
        return firstValue / secondValue
    elif operator == '%':
        return firstValue % secondValue
    else:
        return 0  # Handle unknown operator




coolTestList = input_file_to_string_list("input_RPN_EC.txt")

for line in coolTestList:
    # print(line)
    RPN_expression = RPN_converter(line)
    print(f"Original: {line}")
    print(f"Original Result: {eval(line)}")
    print(f"RPN_Notation {" ".join(RPN_expression)}")
    print(f"RPN Result: {compute_RPN(RPN_expression)}\n")
