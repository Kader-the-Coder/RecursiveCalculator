"""A recursive algorithm to evaluate any algebraic expression."""

#---------------------------IMPORT MODULES-----------------------------
from modules.format_expression import format_expression
from modules.prioritize import prioritize
from modules.simplify import simplify
#-----------------------------FUNCTIONS--------------------------------


def clean_list(expression:list) -> list:
    "Returns a list after removing all empty values"
    return [symbol for symbol in expression if symbol]


def evaluate(expression:str) -> str:
    """Returns the value of an algebraic expression as a string.

    Recursively evaluates an expression, by simplifying a given
    expression one operation per recurse. The recursion ends when the
    expression has no more operations to perform.
    
    * Given expression is converted into a list.
    * A priority list is generated with respect to value.
    * Operation with highest priority is determined.
    * Operation is executed on associated values.
    * Operation and associated values are replaced with prior result.
    * expression is converted back into a string.
    * Steps are repeated until there are no more operations to perform.
    """
    # Format expression for interpretation.
    expression = format_expression(expression)

    # Base case.
    if len(expression) == 1:
        # If value is an integer:
        if int(float(expression[0])) - float(expression[0]) == 0:
            expression = str(int(float(expression[0])))
        else: # If value is decimal:
            expression = str(expression[0])
        return expression

    # Prioritize operations according to BODMAS.
    priority = prioritize(expression)

    # Get index of value with highest priority
    temp_index = priority.index(max(priority))
    # If operation with highest priority is enclosed in parenthesis:
    if expression[temp_index - 2] == "(" and expression[temp_index + 2] == ")":
        expression[temp_index - 2], expression[temp_index + 2] = ["", ""]
        priority[temp_index - 2], priority[temp_index + 2] = ["", ""]
        expression = clean_list(expression)
        priority = clean_list(priority)
    # Get new index of value with highest priority.
    temp_index = priority.index(max(priority))

    # Apply operation with highest priority on operands.
    temp_expression = expression[temp_index - 1:temp_index + 2]
    temp_value = simplify(temp_expression)

    # Replace values that were simplified with the result.
    expression[temp_index - 1], expression[temp_index + 1] = ["", ""]
    expression[temp_index] = temp_value
    expression = clean_list(expression)

    return evaluate("".join(str(symbol) for symbol in expression))


#-----------------------------UNIT TEST--------------------------------

if __name__ == "__main__":
    expressions = [
        "1", "1",
        "(1)", "1",
        "(-1)", "-1",
        "--(-1)", "1",
        "2 + (8 - 4) + 3", "9",
        "3 + 12 * 3 / 12 + 7", "13",
        "(3 + 3) * 42 / (6 + 12)", "14",
        "0.5 - 3.2 * 2.7 - 5", "-13.14",
        "24 - ((32 * 5 / 4 + 1) - 7) - 5", "-15",
        "2-(-1-3)*(-5)", "-18",
        "2 - (-3 + 2 - 5 + (-2 * 3) + 7) / 2", "4.5",
        "-3(4)", "-12"
        ]
    for index in range(0, len(expressions), 2):
        print(f"You got: {evaluate(expressions[index])}, ",
              f"expected answer: {expressions[index + 1]}")
