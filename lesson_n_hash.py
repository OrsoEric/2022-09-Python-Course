import logging
import numbers
from re import X

#hash transform something into a signature number
#needs to be immutable, because hash finds places in a database often
#hash return must never change
#hash is made by professionals. use hash of immutable supported objects to find hash of your object

class Shaka:
    def __init__(self):
        self._immutable = (30,2 )
        self._mutable = [30, 2]

    def __hash__(self):
        """Define the function that compute the hash of the object, If i need the object to be hashable"""
        return hash( self._immutable )

    def __bool__(self):
        """An object can have a condition. e.g. a list return false if empty. Usually bool of an empty constructor is false. If len is defined, bool will be false if len is zero."""
        return self._immutable[0] > 0

    def __call__( self, n_num : numbers.Number ):
        """Turn an object into a callable. FUNCTOR"""
        return self._mutable[0] + n_num



if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    c_test = Shaka()
    logging.debug( hash( c_test ) )
    #this is not hashable
    try:
        logging.debug( hash( [30, 2 ]) )
    except:
        logging.debug( "Unhashable" )


    logging.debug( "Turn into callable: ", c_test( 10 ) )


    pippo = [23, 10]
    
    pluto = pippo + [3, 7]
    #return the unique ID of the object
    print("Original Object", id(pippo))
    print("Created new object", id(pluto))
    pippo += [3, 7]
    print("Reused same object", id(pippo))


    x = [7,3]
    a = x
    b = +x
    print(a is x)
    print(b is x)