"""UNIT TEST"""
#pylint: disable=import-error
#pylint: disable=wrong-import-position
#pylint: disable=invalid-name
import os
import sys
import timeit
DIR = os.path.dirname(__file__)
sys.path.insert(0, DIR.replace("unittests", ""))
from modules.format_expression import format_expression
from modules.prioritize import prioritize
from modules.simplify import simplify
from main import evaluate

# Test tallies
failed = 0
passed = 0
test_num = 0
functions = [format_expression, prioritize, simplify, evaluate]

#======================================================================
expressions = []     # Format for each value in list: {input : expected output}
expressions.append({ # format_expression
    "3(2) + 1 * 4" : ['+3', '*', '(', '+2', ')', '+', '+1', '*', '+4'],
    "-2 + 3(3 - 1) + 2" : ['-2', '+', '+3', '*', '(', '+3', '+', '-1', ')', '+', '+2'],
    })
expressions.append({ # prioritize
    "3(2) + 1 * 4" : [1, 3, 4, 3, 1, 2, 1, 1, 1, 3, 1, 1],
    "-2 + 3(3 - 1) + 2" : [2, 1, 1, 2, 1, 1, 3, 4, 4, 5, 4, 4, 3, 1, 2, 1, 1]
    })
expressions.append({ # simplify
    ("-1", "*", "7"): str(float(-7)),
    ("6", "/", "3"): str(float(2)),
    ("3.4", "+", "2.7"): str(float(6.1)),
    ("8", "-", "-4"): str(float(12)),
    ("(", "-3", ")"): str(float(-3)),
    ("(", "2.8", ")"): str(float(2.8)),
    })
expressions.append({ # evaluate
    "1" : "1",
    "3(2) + 1 * 4" : "10",
    "-2 + 3(3 - 1) + 2" : "6",
    "-3+-3(3 - 1)*3 + (2+1)/7": "-20.57142857"
    })
#======================================================================
while True:
    os.system('cls')
    index = input('''UNITTEST
0 - format_expression
1 - prioritize
2 - simplify
3 - evaluate (main)
e - exit
: ''')
    os.system('cls')
    if index == 'e':
        break
    if not index.isnumeric():
        input("Not valid option")
        continue
    if int(index) >= len(expressions):
        input("Not valid option")
        continue
    index = int(index)
    func = functions[index]
    for expression, expected in expressions[index].items():
        time_start = timeit.default_timer()
        result = func(expression)
        runtime = timeit.default_timer() - time_start
        test_num += 1
        if result != expected:
            print("-"*72)
            print(f">> Test {test_num} Failed.",
                f"expression: {expression}",
                f"returned: {result}",
                f"expected: {expected}",
                f"runtime: {runtime}",
                sep="\n")
            print("-"*72)
            failed += 1
        else:
            print(f">> Test {test_num} Passed.",
                f"Completed in {runtime} seconds.",)
            passed +=1

    print("-"*72)
    print(f"{passed} tests passed.")
    print(f"{failed} tests failed.")
    input("Press ENTER to return to main menu.")
