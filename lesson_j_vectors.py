import logging
from tokenize import Number

class Point_2d:
    """__slot__ destroy the dictionary and prevent fields from being added or removed"""
    __slots__ = ("x", "y")
    def __init__( self, in_x = 0.0, in_y = 0.0 ) -> None:
        self.x = in_x
        self.y = in_y
        logging.debug(f"x {self.x} | y {self.y}")

class Free_vector:
    __slots__ = ("x", "y")
    def __init__( self, in_x = 0.0, in_y = 0.0 ) -> None:
        self.x = in_x
        self.y = in_y
        logging.debug(f"x {self.x} | y {self.y}")

    #overload minority operator
    def __lt__( self, rhs ):
        return (self.x**2 +self.y**2) < (rhs.x**2 +rhs.y**2)

if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    v1 = Free_vector( 3, 4 )
    v2 = Free_vector( 2, 6 )
    print( v1 < v2 )
    print( v2 < v2 )
