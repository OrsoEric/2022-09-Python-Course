import logging

#import user functions as user modules
#import is same as executin
from lesson_a_functions_def import my_function
from my_includes import shaka

#--------------------------------------------------------------------------------------------------------------------------------
#   MAIN
#--------------------------------------------------------------------------------------------------------------------------------

#   if interpreter has the intent of executing this file
if __name__ == "__main__":
    logging.basicConfig( filename="debug.log",level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )
    logging.debug(f"Hello World")
    print("hello world")
    my_function()
    shaka.answer()
