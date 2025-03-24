'''
Alex Nguyen | 1002097417 | amn7417

NOTE: I actually inadvertently implemented the EC first. My sources and approach is explained in the amn7417_Lab03_EC.py, with this being a trimmed version.
'''

import os






# Sources: https://www.geeksforgeeks.org/python-os-open-method/
# https://www.geeksforgeeks.org/with-statement-in-python/
# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
# https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string
'''
input_file_to_string_list
@param
inputFileName: The path to the file as a string

Returns every line of the file as a list
'''
def input_file_to_string_list(inputFileName):
    stringList = []

    # "with" closes file afterwards automatically
    with open(inputFileName, "r") as file:
        stringList = file.readlines()
    
    # Remove excess left/right spaces
    stringList = map(lambda line: line.strip(), stringList)

    return list(stringList)

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




coolTestList = input_file_to_string_list("input_RPN.txt")

for line in coolTestList:
    # print(line)
    print(f"Original: {line}")
    
    print(f"RPN Result: {compute_RPN(RPN_converter(line))}\n")
