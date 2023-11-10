"""
Determine the order in which to simplify a given expression and
then ranks them with greater values having a higher priority
"""


def prioritize(expression:list|str) -> list:
    """Return a numerical list of priorities.

    Determine the order in which to simplify a given expression and
    then ranks them with greater values having a higher priority
    """
    priority = []
    for symbol in expression:
        if symbol in ["(", ")"]:
            priority.append(0)
        elif symbol in ["*", "/"]:
            priority.append(3)
        elif symbol in ["+", "-"]:
            priority.append(2)
        else:
            priority.append(1)

    # Increase priority of symbols in parenthesis
    if "(" in expression:
        # Keep track of nested parentheses.
        parenthesis_open = 0
        parenthesis_close = 0
        index_of_open_parenthesis = expression.index("(")
        for i, value in enumerate(priority, index_of_open_parenthesis):
            parenthesis_open += 1 if value == "(" else 0
            parenthesis_close += 1 if value == ")" else 0
            priority[i] += 3 if value not in ["(", ")"] else 0
            # If closing parenthesis closes parenthesis at index_of_open_parenthesis
            if expression[i] == ")" and parenthesis_open == parenthesis_close:
                return priority
    return priority

#-----------------------------UNIT TEST--------------------------------

if __name__ == "__main__":
    expressions = ['-3', '+', '-18', '+3', '/', '+7']
    #expressions = input(": ")
    print(f"You got: {prioritize(expressions)}")
