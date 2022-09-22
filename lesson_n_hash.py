import logging

#hash transform something into a signature number
#needs to be immutable, because hash finds places in a database often
#hash return must never change

class Shaka:
    def __init__(self):
        self._immutable = (30,2 )
        self._mutable = [30, 2]

    def __hash__(self):
        """Define the function that compute the hash of the object, If i need the object to be hashable"""
        return hash( self._immutable )

    def __bool__(self):
        """An object can have a condition. e.g. a list return false if empty."""
        return self._immutable[0] > 0


if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    c_test = Shaka()
    logging.debug( hash( c_test ) )
    #this is not hashable
    try:
        logging.debug( hash( [30, 2 ]) )
    except:
        logging.debug( "Unhashable" )