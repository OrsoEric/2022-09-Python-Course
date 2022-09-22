import numbers
import logging 

#__complex__(self):

#
class Winding_unwinding():
    """with statement has exit and enter double underscore methods
    useful for classes that need to handle resources
    """
    def __init__(self):
        logging.debug("Init")

    def __enter__(self):
        logging.debug("Enter")

    def __exit__( self, type, value, traceback ):
        logging.debug(f"Exit {type} {value} {traceback} ")

    def __del__(self):
        logging.debug("DIEE!!!!")

if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    with Winding_unwinding() as my_xxx:
        logging.debug(f"We DO!")