"""A recursive algorithm to evaluate any algebraic expression."""

#---------------------------IMPORT MODULES-----------------------------
from modules.utility import list_without_empty_spaces
from modules.format_expression import format_expression
from modules.prioritize import prioritize
from modules.simplify import simplify
#-----------------------------FUNCTIONS--------------------------------


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
        expression = list_without_empty_spaces(expression)
        priority = list_without_empty_spaces(priority)
    # Get new index of value with highest priority.
    temp_index = priority.index(max(priority))

    # Apply operation with highest priority on operands.
    temp_expression =   tuple(expression[temp_index - 1:temp_index + 2])
    temp_value = simplify(temp_expression)

    # Replace values that were simplified with the result.
    expression[temp_index - 1], expression[temp_index + 1] = ["", ""]
    expression[temp_index] = temp_value
    expression = list_without_empty_spaces(expression)

    return evaluate("".join(str(symbol) for symbol in expression))


#-----------------------------UNIT TEST--------------------------------

if __name__ == "__main__":
    while True:
        expressions = input(": ")
        print(f"You got: {evaluate(expressions)}")
