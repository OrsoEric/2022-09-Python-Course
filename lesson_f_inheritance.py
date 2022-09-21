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
    def __init__( self, is_color = None ):
        #constructor of base class is not called by default
        super().__init__()
        logging.debug("Init Pixel")
        if is_color is None:
            self.color = "Black"
        else:
            self.color = is_color

#   if interpreter has the intent of executing this file
if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )
    logging.debug(f"Start...")

    c_origin = Point_2d()
    #print( "Name Mangling", c_origin.__dict__ )


