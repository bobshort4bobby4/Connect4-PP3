"""
Module containing mixin Class used to clear terminal screen

Classes: ClearMixin
"""


import os


class ClearMixin():
    """
    A mixin function to clear the screen  copy/paste from codecap.org

    Parameters: None

    Variables: None

    Returns: None.
    """
    @staticmethod
    def clrscr():  # Check if Operating System is Mac and Linux or Windows
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')
