import os


class ClearMixin():
    """
    A function to clear the screen  copy/paste from codecap.org
    """
    @staticmethod   
    def clrscr():  # Check if Operating System is Mac and Linux or Windows 
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # Else Operating System is Windows (os.name = nt)
            _ = os.system('cls')