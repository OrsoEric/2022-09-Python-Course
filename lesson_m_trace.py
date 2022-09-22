import logging
import numbers
import math 

class Point_2d:
    """__slot__ destroy the dictionary and prevent fields from being added or removed"""
    __slots__ = ("x", "y")
    def __init__( self, in_x : numbers.Number= 0.0, in_y : numbers.Number = 0.0 ) -> None:
        self.x = in_x
        self.y = in_y
        logging.debug(f"x {self.x} | y {self.y}")

class Free_vector:
    """free vector"""
    __slots__ = ("x", "y")
    def __init__( self, in_x : numbers.Number= 0.0, in_y : numbers.Number = 0.0 ) -> None:
        self.x = in_x
        self.y = in_y
        logging.debug(f"x {self.x} | y {self.y}")

    def __lt__( self, rhs : "Free_vector" ):
        """overload minority operator"""
        if isinstance(rhs, Free_vector):
            return (self.x**2 +self.y**2) < (rhs.x**2 +rhs.y**2)
        #I can detect types in runtime
        elif isinstance(rhs, numbers.Number ):
            return (self.x**2 +self.y**2) < (rhs)
        else:
            return False

    def __eq__( self, rhs : "Free_vector" ):
        """overload minority operator"""
        if isinstance(rhs, Free_vector):
            #real are almost never the same. sqrt(2)**2 == 2
            return math.isclose((self.x**2 +self.y**2), (rhs.x**2 +rhs.y**2) )
        #I can detect types in runtime
        elif isinstance(rhs, numbers.Number ):
            return (self.x**2 +self.y**2) < (rhs)
        else:
            return False


    #cannot overload because python doesn't know numbers
    #def __lt__( self, rhs : numbers.Number ):
    #    """overload minority operator"""
    #    return (self.x**2 +self.y**2) < (rhs)

if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )
    
    v1 = Free_vector( 3, 4 )
    v2 = Free_vector( 2, 6 )
    print( v1 < v2 )
    print( v2 < v2 )

    print( v2 < 4 )



