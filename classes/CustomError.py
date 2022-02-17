"""
Module containing custom error Class and Base Class

Classes:
Error

ColumnFullError.
"""


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ColumnFullError(Error):
    """ Error raised when a playing column is full"""
    pass