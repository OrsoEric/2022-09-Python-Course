import logging

class Point_2d:
    """__slot__ destroy the dictionary and prevent fields from being added or removed"""
    __slots__ = ("x", "y")
    def __init__( self, in_x = 0.0, in_y = 0.0 ):
        logging.debug("Init Point2D")
        self.x = in_x
        self.y = in_y
        #print(f"slots remove dict: {self.__dict__}")


class Pixel(Point_2d ):
    """A colored 2D point"""
    __slots__ = ("color")
    def __init__( self, iln_color = None ):
        #constructor of base class is not called by default
        super().__init__()
        logging.debug("Init Pixel")
        if iln_color is None:
            self.color = (0,0,0)
        else:
            self.color = iln_color

    def dim( self, in_dim ):
        """Dim by a divisor"""
        self.color = (self.color[0]*in_dim, self.color[1]*in_dim, self.color[2]*in_dim)

    def __str__( self ):
        """stringification method"""
        return f"{self.color[0]} {self.color[1]} {self.color[2]}"

#   if interpreter has the intent of executing this file
if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )
    logging.debug(f"Start...")

    c_origin = Point_2d()
    #print( "Name Mangling", c_origin.__dict__ )

if __name__ == "__main__":
    print("method can be before and after point")

    print( "-".join("xyz") )
    print( "-".join(["x","y","z"]) )
    print( str.join("-",["x","y","z"]) )

    my_pixel = Pixel( (255, 127, 30) )
    print(my_pixel.color)
    #call method directly
    my_pixel.dim( 0.5 )
    print(my_pixel.color)
    #call class method and provide the self externally
    Pixel.dim( my_pixel, 0.5 )
    print(my_pixel.color)

    print( Pixel.__dir__(my_pixel) )

    print("Stringification methoid of class __str__")
    print( my_pixel )
    print( str(my_pixel))
    print( my_pixel.__str__() )
    #Show what obkect is. repr can be overloaded as well
    print(f"{repr(Pixel())}")

