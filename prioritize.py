def prioritize(expression:list) -> list:
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
    expressions = [
        "1", [1],
        "(1)", [3, 4, 3],
        "(-1)", [3, 5, 4, 3],
        "--(-1)", [2, 2, 3, 5, 4, 3],
        "2 + (8 - 4) + 3", [1, 1, 2, 1, 3, 4, 4, 5, 4, 4, 3, 1, 2, 1, 1],
        "3 + 12 * 3 / 12 + 7", [1, 1, 2, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 1, 2, 1, 1],
        "(3 + 3) * 42 / (6 + 12)", [3, 4, 4, 5, 4, 4, 3, 1, 3, 1, 1, 1, 1, 3, 1, 0, 1, 1, 2, 1, 1, 1, 0],
        "0.5 - 3.2 * 2.7 - 5", [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1],
        "24 - ((32 * 5 / 4 + 1) - 7) - 5", [1, 1, 1, 2, 1, 3, 3, 4, 4, 4, 6, 4, 4, 4, 6, 4, 4, 4, 5, 4, 4, 3, 1, 2, 1, 1, 0, 1, 2, 1, 1],
        "2-(-1-3)*(-5)", [1, 2, 3, 5, 4, 5, 4, 3, 3, 0, 2, 1, 0],
        "2 - (-3 + 2 - 5 + (-2 * 3) + 7) / 2", [1, 1, 2, 1, 3, 5, 4, 4, 5, 4, 4, 4, 5, 4, 4, 4, 5, 4, 3, 5, 4, 4, 6, 4, 4, 3, 1, 2, 1, 1, 0, 1, 3, 1, 1]
        ]
    for index in range(0, len(expressions), 2):
        print(f"{prioritize(expressions[index])} <- Output, \n",
              f"{expressions[index + 1]} <- Expected output\n", sep="")