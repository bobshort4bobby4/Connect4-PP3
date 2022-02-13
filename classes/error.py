class Error(Exception):
    """Base class for other exceptions"""
    pass


class ColumnFullError(Error):
    """Raised when the column is full"""
    pass