"""
Converts a supplied string to a list, with each value of the list
being a character in the string. The list will contain no empty values.
"""


#-----------------------------FUNCTIONS--------------------------------
#pylint: disable=used-before-assignment

def __convert_to_list(expression):
    """Convert string to list"""
    current_symbol = [" ", "[", "]", "(", ")", "*", "/", "+", "-", ",", "  "]
    new_symbol = ["", "(", ")", " ( ", " ) ", " * ", " / ", " + ", " - ", ".", " "]
    for i, symbol in enumerate(current_symbol):
        expression = expression.replace(symbol, new_symbol[i])
    expression = expression.strip().split()
    return list_without_empty_spaces(expression)


def __resolve_symbols(expression):
    """Resolve symbols double positive and negative symbols """
    is_sum = False  # True if there must be a '+' between symbols.
    for i, symbol in enumerate(expression):
        # Determine if symbols must be separated by a "+" operator.
        if symbol[-1].isnumeric() or symbol == ")":
            is_sum = not is_sum
        if symbol in ["(", "*", "/"]:
            is_sum = False
        if symbol in ["+", "-"] and expression[i - 1] == ")":
            is_sum = True
        # Simplify repeating "+" and "-" operators and change
        # subtraction operators to addition of negative integers.
        if symbol in ["-", "+"]:
            if expression[i + 1][-1].isnumeric():
                expression[i + 1] = "".join([symbol, expression[i + 1]])
                expression[i] = "+" if is_sum else ""
            elif expression[i + 1] in ["-", "+"]:
                expression[i + 1] = "+" if expression[i + 1] == symbol else "-"
                expression[i] = ""
    return list_without_empty_spaces(expression)


def __resolve_parenthesis(expression):
    """Insert '*' between values and '('."""
    index_of_bracket = []
    for i, symbol in enumerate(expression):
        if symbol == "(" and i != 0:
            # [-1] to look only at last value
            if expression[i - 1][-1].isnumeric():
                index_of_bracket.append(i + len(index_of_bracket))
    for i in index_of_bracket:
        expression.insert(i,"*")
    return expression


def format_expression(expression:str) -> list:
    """Formats and the returns a given expression as a list"""
    expression = __convert_to_list(expression)
    expression = __resolve_symbols(expression)
    expression = __resolve_parenthesis(expression)
    # Remove all empty values and then return list.
    return expression


#-----------------------------UNIT TEST--------------------------------

if __name__ == "__main__":
    from utility import list_without_empty_spaces
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
        "2 - (-3 + 2 - 5 + (-2 * 3) + 7) / 2", ['2', '-', '(', '-3', '+', '+2', '-5', '+', '(', '-2', '*', '3', ')', '+', '+7', ')', '/', '2'],  #pylint: disable=line-too-long
        "[-3 + (2 - 7) / 2] - 3", ['(', '-3', '+', '(', '2', '+', '-7', ')', '/', '2', ')', '+', '-3'],     #pylint: disable=line-too-long
        "2(3 + 1)", ['2', '*', '(', '3', '+', '+1', ')'],
        "[3 + 3(1 + 2)]", ['(', '3', '+', '+3', '*', '(', '1', '+', '+2', ')', ')'],
        "3(2+1)", ['3', '*', '(', '2', '+', '+1', ')'],
        "3(2+(1+3))", ['3', '*', '(', '2', '+', '(', '1', '+', '+3', ')', ')'],
        "3(-2(-1)))", ['3', '*', '(', '-2', '*', '(', '-1', ')', ')', ')'],
        "3(2) + 1", ['3', '*', '(', '2', ')', '+', '+1']
        ]
    for index in range(0, len(expressions), 2):
        print(f"{expressions[index]} <- Input")
        print(f"{format_expression(expressions[index])} <- Output\n",
              f"{expressions[index + 1]} <- Expected output", sep="")
        if format_expression(expressions[index]) == expressions[index + 1]:
            print("passed\n")
        else:
            print("failed\n")
    while True:
        expressions = input(": ")
        print(f"You got: {format_expression(expressions)}")
