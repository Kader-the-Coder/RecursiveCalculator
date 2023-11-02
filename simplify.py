"""Simplifies an expression with a single operator."""

def simplify(expression:list) -> str:
    """Returns the value of a simple expression

    * expression: A list with format [value1, operator, value2].
    """
    if expression[1][-1].isnumeric(): # ["(", "value", ")"]
        expression = str(expression[1])
    elif expression[1] == "*":
        expression = float(expression[0]) * float(expression[2])
    elif expression[1] == "/":
        expression = float(expression[0]) / float(expression[2])
    elif expression[1] == "+":
        expression = float(expression[0]) + float(expression[2])
    elif expression[1] == "-":
        expression = float(expression[0]) - float(expression[2])
    return str(expression)

#-----------------------------UNIT TEST--------------------------------

if __name__ == "__main__":
    expressions = [
        ["-1", "*", "7"], str(float(-7)),
        ["6", "/", "3"], str(float(2)),
        ["3.4", "+", "2.7"], str(float(6.1)),
        ["8", "-", "-4"], str(float(12)),
        ["(", "-3", ")"], str(float(-3)),
        ["(", "2.8", ")"], str(float(2.8)),
        ]
    for index in range(0, len(expressions), 2):
        print(f"You got: {simplify(expressions[index])}, ",
              f"expected answer: {expressions[index + 1]}")