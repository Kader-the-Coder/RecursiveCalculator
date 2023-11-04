"""Utility modules"""


def list_without_empty_spaces(expression:list) -> list:
    "Returns a list after removing all empty values"
    return [symbol for symbol in expression if symbol]