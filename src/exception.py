import sys

# Function to format the error message
def error_msg(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error_message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class
class CustomeException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Corrected: using super() to call the parent class constructor
        self.error_message = error_msg(error_message, error_detail)  # Corrected the parameter name

    def __str__(self):
        return self.error_message
