"""
Alex Nguyen
1002097417
Windows 11
Python 3.13.2
"""



# Take in input.txt, a java program


# 1. List the nesting depth of curly braces
# 2. Ignore braces insides quotes or cokmments
# 3. Test for unmatched braces ( expected  '}' but found EOF); Output an error message
# 4. Allow for multiple braces on the same line, for example "}}" ending a loop and a function
# 5. Handle block comments that cross multiple lines of the input file.

'''
Approach:

Get lines from inputs.
Interate through each character from each line
Order of operations:
    Check for comments
    Check for quotes
    Check for bracket
Implement ignoring of comments and quotes (first in the order of operations)
Print out each line iteratively of the formatted output

'''
def block_depth(input_file_name = "input.txt"):
    # input_file_name = "input.txt"
    tokenized_input = []
    with open(input_file_name, "r") as file:
        tokenized_input = file.readlines()

    # print(tokenized_input) // After checking input, the readlines read lines (duh) including the new character at the end. 


    depth = 0
    in_comment = False
    in_string = False
    stack = []  # Stack to keep track of opening braces and subsequently matching closed braces

    for line_number, line in enumerate(tokenized_input, 1):
        original_line = line                                       
        # print("original line: " + original_line)
        annotated_line = ""

        i = 0 # in order to parse, must look at each character individually 
        while i < len(line):
            char = line[i]

            # Requirement 2 of ignoring comments
            if in_comment:
                if char == '*' and i + 1 < len(line) and line[i + 1] == '/':
                    in_comment = False
                    i += 1  # Consume the '/'
                i += 1
                continue
            
            # Requirement 2 of ignoring quotes
            elif in_string:
                if char == '"':
                    in_string = False
                i += 1
                continue

            # Comment detection logic
            elif char == '/':
                # Requirement 5 for block comments
                if i + 1 < len(line) and line[i + 1] == '*': # Multiline comment case
                    in_comment = True
                    i += 1  # Consume the '*'
                    i += 1
                    continue
                # Requirement 2 of ignoring comments
                elif i + 1 < len(line) and line[i + 1] == '/': # Singleline comment case
                    # Since in a single line comment, ignore the entire line
                    break
                else: # Everything else that isn't a comment of some kind
                    i+=1 

            # Quote detection logic
            elif char == '"':
                in_string = True
                i += 1
                continue

            # Requirement 1: Bracket detection 
            elif char == '{':
                depth += 1
                stack.append((char, line_number))  # Requirement 1: Store opening brace and line number
                i += 1

            # Requirement 3: Matching closed bracket detection
            elif char == '}':
                if depth > 0: # Since block is closed, must be one less of the lever
                    depth -= 1
                    stack.pop()  # Remove matching opening brace
                else: # Case where depth = 0 but closed bracket encountered 
                    print(f"Error: Unmatched '}}' at line {line_number}")
                i += 1
            
            # Letter is none of the edge cases, in which case continue parsing through the line
            else:
                i += 1
        annotated_line = f"{depth} {original_line}"
        print(annotated_line)

    if stack:
        # Check for any unclosed braces
        for brace, line_num in stack:
            # Requirement 3: Error message for unmatched brace
            print(f"Error: Expected '}}' but found EOF at line {line_num}") # For some reason, in order to print a single }, one must use }}

block_depth()



