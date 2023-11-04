"""
Converts a supplied string to a list, with each value of the list
being a character in the string. The list will contain no empty values.
"""

def _convert_to_list(expression):
    """Resolve symbols (-- and ++ )"""
    old_symbol = [" ", "[", "]", "(", ")", "*", "/", "+", "-", ",", "  "]
    new_symbol = ["", "(", ")", " ( ", " ) ", " * ", " / ", " + ", " - ", ".", " "]
    for i, symbol in enumerate(old_symbol):
        expression = expression.replace(symbol, new_symbol[i])
    expression = expression.strip()
    expression = expression.split()
    return expression


def _resolve_symbols(expression):
    """Resolve symbols (-- and ++ )"""
    # Resolve symbols (-- and ++ )
    is_sum = False  # check if values must be joined with a "+"
    for i, symbol in enumerate(expression):
        # Check if symbols must be separated by a "+" operator.
        if symbol[-1].isnumeric() or symbol == ")":
            is_sum = not is_sum
        if symbol in ["(", "*", "/"]:
            is_sum = False
        # Simplify repeating "+" and "-" operators and change
        # subtraction operators to addition of negative integers.
        if symbol in ["-", "+"]:
            if expression[i + 1][-1].isnumeric():
                expression[i + 1] = "".join([symbol, expression[i + 1]])
                expression[i] = "+" if is_sum else ""
            elif expression[i + 1] in ["-", "+"]:
                expression[i + 1] = "+" if expression[i + 1] == symbol else "-"
                expression[i] = ""
    return expression


def _resolve_parenthesis(expression):
    """Insert '*' between values and "("."""
    index_of_bracket = []
    for i, symbol in enumerate(expression):
        if symbol == "(" and i != 0:
            # [-1] to look only at last value
            if expression[i - 1][-1].isnumeric():
                index_of_bracket.append(i)
    for index in index_of_bracket:
        expression.insert(index,"*")
    return expression


def format_expression(expression:str) -> list:
    """Formats and the returns a given expression as a list"""
    expression = _convert_to_list(expression)
    expression = _resolve_symbols(expression)
    expression = _resolve_parenthesis(expression)
    # Remove all empty values and then return list.
    return [symbol for symbol in expression if symbol]


#-----------------------------UNIT TEST--------------------------------

if __name__ == "__main__":
    expressions = [
        "1", ['1'],
        "2(3)", ['2', '*', '(', '3', ')'],
        "(-1)", ['(', '-1', ')'],
        "--(-1)", ['+', '(', '-1', ')'],
        "2 + (8 - 4) + 3", ['2', '+', '(', '8', '+', '-4', ')', '+', '+3'],
        "3 + 12 * 3 / 12 + 7", ['3', '+', '+12', '*', '3', '/', '12', '+', '+7'],
        "(3 + 3) * 42 / (6 + 12)", ['(', '3', '+', '+3', ')', '*', '42', '/', '(', '6', '+', '+12', ')'],   #pylint: disable=line-too-long
        "0.5 - 3.2 * 2.7 - 5", ['0.5', '+', '-3.2', '*', '2.7', '+', '-5'],
        "24 - ((32 * 5 / 4 + 1) - 7) - 5", ['24', '-', '(', '(', '32', '*', '5', '/', '4', '+', '+1', ')', '+', '-7', ')', '+', '-5'],  #pylint: disable=line-too-long
        "2-(-1-3)*(-5)", ['2', '-', '(', '-1', '+', '-3', ')', '*', '(', '-5', ')'],
        "2 - (-3 + 2 - 5 + (-2 * 3) + 7) / 2", ['2', '-', '(', '-3', '+', '+2', '-5', '+', '(', '-2', '*', '3', ')', '+7', ')', '/', '2'],  #pylint: disable=line-too-long
        "[-3 + (2 - 7) / 2] - 3", ['(', '-3', '+', '(', '2', '+', '-7', ')', '/', '2', ')', '-3'],
        "2(3 + 1)", ['2', '*', '(', '3', '+', '+1', ')'],
        "[3 + 3(1 + 2)]", ['(', '3', '+', '+3', '*', '(', '1', '+', '+2', ')', ')']
        ]
    for i in range(0, len(expressions), 2):
        print(f"{expressions[i]} <- Input")
        print(f"{format_expression(expressions[i])} <- Output, \n",
              f"{expressions[i + 1]} <- Expected output", sep="")
        if format_expression(expressions[i]) == expressions[i + 1]:
            print("passed\n")
        else:
            print("failed\n")
