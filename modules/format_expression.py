"""
Converts a supplied string to a list, with each value of the list
being a character in the string. The list will contain no empty values.
"""

#-----------------------------FUNCTIONS--------------------------------


def __convert_to_list(expression):
    """Convert string to list"""
    current_symbol = [" ", "[", "]", "(", ")", "*", "/", "+", "-", ",", "  "]
    new_symbol = ["", "(", ")", " ( ", " ) ", " * ", " / ", " + ", " - ", ".", " "]
    for i, symbol in enumerate(current_symbol):
        expression = expression.replace(symbol, new_symbol[i])
    expression = expression.strip().split()
    return [symbol for symbol in expression if symbol]


def __resolve_symbols(expression):
    """Resolve symbols double positive and negative symbols """
    is_sum = False  # True if there must be a '+' between symbols.
    for i, symbol in enumerate(expression):
        # Determine if symbols must be separated by a "+" operator.
        if not symbol[-1].isnumeric() or symbol != ")":
            is_sum = True
        if symbol in ["(", "*", "/"]:
            is_sum = False
        if expression[i - 1] == "(":
            is_sum = False
        if symbol in ["+", "-"] and expression[i - 1] == ")":
            is_sum = True
        # Simplify repeating "+" and "-" operators and change
        # subtraction operators to addition of negative integers.
        if symbol in ["-", "+"]:
            if expression[i + 1][-1].isnumeric():
                expression[i + 1] = "".join([symbol, expression[i + 1]])
                if is_sum and i != 0:
                    expression[i] = "+"
                if expression[i - 1] in ["*", "/"] and i != 0:
                    expression[i] = ""
                    continue
                elif is_sum:
                    expression[i] = "+" if i != 0 else ""
                    continue
                expression[i] = ""
            elif expression[i + 1] in ["-", "+"]:
                expression[i + 1] = "+" if expression[i + 1] == symbol else "-"
                expression[i] = ""
    for i, symbol in enumerate(expression):
        if symbol.isnumeric():
            expression[i] = f"+{expression[i]}"
    return [symbol for symbol in expression if symbol]


def __resolve_parenthesis(expression:list):
    """Insert '*' between values and '('."""
    index_of_bracket = []
    if "(" not in expression:
        return expression
    
    # Keep track of nested parentheses.
    parenthesis_open = 0
    parenthesis_close = 0
    for i, symbol in enumerate(expression):
        parenthesis_open += 1 if symbol == "(" else 0
        parenthesis_close += 1 if symbol == ")" else 0
        if symbol == "(" and i != 0:
            # [-1] to look only at last value
            if expression[i - 1][-1].isnumeric():
                index_of_bracket.append(i + len(index_of_bracket))
    for i in index_of_bracket:
        expression.insert(i,"*")
    parenthesis_number = parenthesis_open - parenthesis_close
    for i in range(abs(parenthesis_number)):
        if parenthesis_number > 0:
            expression.append(")")
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
    while True:
        expressions = input(": ")
        print(f"Input: {expressions}")
        print(f"Output: {format_expression(expressions)}\n")
