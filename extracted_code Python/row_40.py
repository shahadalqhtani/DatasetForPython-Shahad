import traceback
import sys

class FullStackTraceException(Exception):
    def __init__(self, message, *args):
        super().__init__(message, *args)
        self.full_traceback = None

    def with_traceback(self, tb):
        self.full_traceback = traceback.format_tb(tb)
        return self

def custom_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, FullStackTraceException):
        # Handle the exception by returning a detailed error message
        error_message = f"An error occurred: {exc_value}"
        full_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback)
        local_vars = sys._getframe().f_locals.copy()
        return error_message, full_traceback, local_vars
    else:
        # Re-raise the exception by default
        raise exc_value

# Set the custom exception handler
sys.excepthook = custom_exception_handler

# Example usage of FullStackTraceException
try:
    x = 1 / 0
except ZeroDivisionError as e:
    raise FullStackTraceException("Something went wrong", e).with_traceback(e.__traceback__)