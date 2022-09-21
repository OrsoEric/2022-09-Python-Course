
class Point_2d:
    """__slot__ destroy the dictionary and prevent fields from being added or removed"""
    __slots__ = ("x", "y")
    def __init__( self, in_x = 0.0, in_y = 0.0 ):
        self.x = in_x
        self.y = in_y
        #print(f"slots remove dict: {self.__dict__}")

    @property
    def quadrant(self):
        if self.x>=0 and self.y>=0:
            return 0
        elif self.x>=0 and self.y<0:
            return 1
        elif self.x<0 and self.y>=0:
            return 2
        elif self.x<0 and self.y<0:
            return 3
        else:
            return None


#   if interpreter has the intent of executing this file
if __name__ == "__main__":

    c_point = Point_2d()
    #I can no longer add items
    #c_point.shaka = 3
    print( c_point.quadrant )