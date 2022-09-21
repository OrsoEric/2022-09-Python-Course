import logging
from tokenize import Number

#I can have snow wheels on electric cars

class Wheel:
    def __init__( self, is_manufacturer : str = None ):
        
        if is_manufacturer is None:
            self._s_manufacturer = "?"
        else:
            self._s_manufacturer = is_manufacturer
        logging.debug(f"{ Wheel.__str__(self)}")

    def __str__( self ):
        return f"Manufacturer: {self._s_manufacturer}"


class Snow_wheel( Wheel ):
    def __init__( self, *arg ):
        logging.debug( f"Wheel arguments: {arg}")
        super().__init__( arg )
        logging.debug("Snow Wheel")

class Car():
    
    pass

class Electric_car( Car ):
    #I can pass the class as parameter
    def __init__( self, ic_wheel_type : object = None, *arg ):
        if (ic_wheel_type is None):
            self._c_wheel = None
        else:
            #I can construct the class
            self._c_wheel = ic_wheel_type.__init__( arg )

if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    my_wheel = Wheel( "Goodyear" )


    my_car = Electric_car()
    my_car = Electric_car( Wheel(), "Pirelli" )
    my_car = Electric_car( Snow_wheel(), "PirelliS" )