"""
Build an arithmetic calculator
"""

def arithmetic_arranger(problems, show_answers=False):

    first_line = []
    second_line = []
    separator = []
    solution_line = []
    

    if len(problems)>5:
        return 'Error: Too many problems.'

    for problem in problems:
        splited_problem = problem.split()
        operand1 = splited_problem[0]
        operator = splited_problem[1]
        operand2 = splited_problem[2]

        if operator != "-" and operator != "+":
            return "Error: Operator must be '+' or '-'"

        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(operand1)>4 or len(operand2)>4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max((len(operand1),len(operand2))) + 2
        first_line.append(operand1.rjust(width))
       # print (first_line)
        second_line.append(operator+" "+operand2.rjust(width-2))
       # print (second_line)
        separator.append("-" * width)

        
    
        if show_answers:
            if operator == "+":
                solution = int(operand1) + int(operand2)
            elif operator == "-":
                solution = int(operand1) - int(operand2)

            solution_line.append(str(solution).rjust(width))
                
    print(first_line)
    print(second_line)
    
    join_line = "  ".join(first_line) + "\n" + "  ".join(second_line) + "\n" + "  ".join(separator) + "\n" + "  ".join(solution_line)   

    return join_line                    


def main():
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
    

main()
