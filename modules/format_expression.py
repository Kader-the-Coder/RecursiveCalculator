"""
Converts a supplied string to a list, with each value of the list
being a character in the string. The list will contain no empty values.
"""

def format_expression(expression:str) -> list:
    """Converts a string to a list."""
    expression = expression.replace(" ","")
    expression = expression.replace("[","(")
    expression = expression.replace("("," ( ")
    expression = expression.replace(")"," ) ")
    expression = expression.replace("*"," * ")
    expression = expression.replace("/"," / ")
    expression = expression.replace("+"," + ")
    expression = expression.replace("-"," - ")
    expression = expression.replace(","," . ")
    expression = expression.replace("  "," ")
    expression = expression.strip()
    expression = expression.split()

    is_sum = False  # check if values must be joined with a "+"
    for i, symbol in enumerate(expression):
        # Check if symbols must be separated by a "+" operator.
        if symbol[-1].isnumeric() or symbol == ")":
            is_sum = not is_sum
        if symbol in ["(", "*", "/"]:
            is_sum = False
        # Simplify repeating "+" and "-" operators
        if symbol in ["-", "+"]:
            if expression[i + 1][-1].isnumeric():
                expression[i + 1] = "".join([symbol, expression[i + 1]])
                expression[i] = "+" if is_sum else ""
            elif expression[i + 1] in ["-", "+"]:
                expression[i + 1] = "+" if expression[i + 1] == symbol else "-"
                expression[i] = ""
    # Remove all empty values and then return list\
    return [symbol for symbol in expression if symbol]

#-----------------------------UNIT TEST--------------------------------

if __name__ == "__main__":
    expressions = [
        "1", ['1'],
        "(1)", ['(', '1', ')'],
        "(-1)", ['(', '-1', ')'],
        "--(-1)", ['+', '(', '-1', ')'],
        "2 + (8 - 4) + 3", ['2', '+', '(', '8', '+', '-4', ')', '+', '+3'],
        "3 + 12 * 3 / 12 + 7", ['3', '+', '+12', '*', '3', '/', '12', '+', '+7'],
        "(3 + 3) * 42 / (6 + 12)", ['(', '3', '+', '+3', ')', '*', '42', '/', '(', '6', '+', '+12', ')'],
        "0.5 - 3.2 * 2.7 - 5", ['0.5', '+', '-3.2', '*', '2.7', '+', '-5'],
        "24 - ((32 * 5 / 4 + 1) - 7) - 5", ['24', '-', '(', '(', '32', '*', '5', '/', '4', '+', '+1', ')', '+', '-7', ')', '+', '-5'],
        "2-(-1-3)*(-5)", ['2', '-', '(', '-1', '+', '-3', ')', '*', '(', '-5', ')'],
        "2 - (-3 + 2 - 5 + (-2 * 3) + 7) / 2", ['2', '-', '(', '-3', '+', '+2', '-5', '+', '(', '-2', '*', '3', ')', '+7', ')', '/', '2']
        ]
    for index in range(0, len(expressions), 2):
        print(f"{format_expression(expressions[index])} <- Output, \n",
              f"{expressions[index + 1]} <- Expected output\n", sep="")