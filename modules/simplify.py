"""Simplifies an expression with a single operator."""

def simplify(expression:tuple) -> str:
    """Returns the value of a simple expression

    * expression: A tuple with format ("value1", "operator", "value2").
    """
    if expression[1][-1].isnumeric(): # ("(", "value", ")")
        expression = str(float(expression[1]))
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
    expressions = ('+3', '/', '+7')
    #expressions = input(": ")
    print(f"You got: {simplify(expressions)}")

