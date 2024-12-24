def arithmetic_arranger(problems,show_answers= False):
    
    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []
    
    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
       # print (parts)
        num1 = parts[0]
        #print(num1)
        operator = parts[1]
        num2 = parts[2]
       # print(num2)
        
        # Check if the operands have more than 4 digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "*" or operator == "/":
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'

        # Calculate the width for formatting (the longer number + 2 for operator and space)
        width = max(len(num1), len(num2)) + 2
        
        # Append formatted parts to the respective lines
        first_line.append(num1.rjust(width))
        #print (first_line)
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        dash_line.append('-' * width)

        if show_answers:
            if operator == "+":
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_line.append(answer.rjust(width))
    
    # Join the formatted parts with 4 spaces between each problem
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dash_line) + '\n' + '    '.join(answer_line)

   
    return arranged_problems

# Test the function

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print()
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
