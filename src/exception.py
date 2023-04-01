import sys

"""reason of use sys in below
In the line 'error, error_detail: sys', 'sys' is used to 
specify the type of the 'error_detail' argument.

'sys' is a built-in Python module that provides 
access to some variables and functions related to 
the Python interpreter. In this code, 'sys' is used 
to specify that the 'error_detail' argument should be
 a 'sys' object that contains information about the 
 error that caused the exception.

The 'error_detail' argument is expected to be 
a 'sys.exc_info()' object, which is a tuple containing
 information about the current exception that is being 
 handled. This object has three elements: the type of
 the exception, the exception instance itself, and the
 traceback object that contains information about the
 call stack at the point where the exception was raised.

So, the 'error_detail' argument is expected to be 
a 'sys.exc_info()' object, which is a standard way of 
getting information about the current exception in Python."""

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


"""for testing this code
import logging
if __name__=="__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide By Zero")
        raise CustomException(e,sys)"""


"""some theoritical concept
This code defines a custom exception class called
 'CustomException' that takes an error message and
  an error detail object as arguments. The 
  'error_message' argument is passed to the 
  superclass constructor using 
  'super().__init__(error_message)', 
  which sets the error message for the exception.

The 'error_detail' argument is expected to be 
a 'sys' object that contains information about
 the error that caused the exception. Specifically, 
 the 'error_message_detail' function is called with 
 the 'error_message' and 'error_detail' arguments to
  create a detailed error message string that includes 
  the name of the Python script, the line number where 
  the error occurred, and the error message itself.

The '__str__' method of the 'CustomException' class 
returns the detailed error message string, so that 
it can be displayed when the exception is raised.

The 'error_message_detail' function takes an error
 message and an error detail object as arguments. It uses
  the 'exc_info()' method of the 'error_detail' object 
  to get information about the current exception, 
  including the traceback object ('exc_tb'). It then 
  uses the 'tb_frame' attribute of the traceback object 
  to get information about the current frame, including
   the filename ('co_filename') and line number 
   ('tb_lineno'). Finally, it formats a string containing
    the filename, line number, and error message, and returns it."""