"""UNIT TEST"""
#pylint: disable=import-error
#pylint: disable=wrong-import-position
#pylint: disable=invalid-name

#===========================IMPORT LIBRARIES===========================

import os
import sys
import json
import timeit
import traceback

#============================IMPORT MODULES============================

DIR = os.path.dirname(__file__)
sys.path.insert(0, DIR.replace("unittests", ""))
from modules.format_expression import format_expression
from modules.prioritize import prioritize
from modules.simplify import simplify
from main import evaluate

#=========================INITIALIZE VARIABLES=========================

unittestsfile = f"{DIR}\\unittests.json"
func = [format_expression, prioritize, simplify, evaluate]
func_string = ["format_expression", "prioritize", "simplify", "evaluate"]

#===========================DEFINE FUNCTIONS===========================


def run_test(function, index, expressions):
    """Runs a given function"""
    os.system('cls')
    failed, passed, test_num = 0, 0, 0
    print(f"running {function.__name__}", "-" * 72, sep="\n")
    for expression, expected in expressions.items():
        time_start = timeit.default_timer()
        try:
            if index == 1:  # prioritize
                expression = expression.split(" ")
            if index == 2:  # simplify
                expression = expression.replace(" ","").split(",")
                expected = str(float(expected))
            result = function(expression)
        except BaseException:   #pylint: disable=broad-exception-caught
            result = traceback.format_exc()
        runtime = timeit.default_timer() - time_start
        test_num += 1
        if result != expected:
            print("-"*72)
            print(f">> Test {test_num} Failed.",
                f"expression: {expression}",
                f"returned: {result}{type(result)}",
                f"expected: {expected}{type(expected)}",
                f"Completed in {runtime}",
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


def menu():
    """Main function for selecting test to perform"""
    index = input('''UNITTEST
-----------------------------------------------------------------------
0 - format_expression
1 - prioritize
2 - simplify
3 - evaluate (main)
e - exit
: ''')

    if index == 'e':
        os.system('cls')
        return False
    if not index.isnumeric():
        print("Not valid option")
        return True
    if int(index) >= len(func):
        print("Not valid option")
        return True

    with open(unittestsfile, "r", encoding="utf-8") as file:
        data = json.load(file)
    index = int(index)
    function = func[index]
    expressions = data[func_string[index]]
    run_test(function, index, expressions)

    return True

#===============================RUN MODULE=============================

os.system('cls')
while menu():
    input("\nPress ENTER to return to main menu.")
    os.system('cls')
