#Excercise
#1) create object wheel
#2) create object veichle that has a number of wheels
#

#Excercise Electric veichle battery

import logging
import numbers
from tokenize import Number

class Wheel:
    """Wheel of a veichle"""
    def __init__( self, is_manufacturer :str = None, in_diameter : Number = None  ):
        """Empty Constructor
        Args:
            is_manufacturer (str, optional): brand of the wheel . Defaults to None.
            in_diameter (Number, optional): [description]. Defaults to None.
        """
        if (is_manufacturer is None):
            self.__s_manufacturer = "?"
        else:
            self.__s_manufacturer = is_manufacturer
        #diameter of the wheel
        if (in_diameter is None):
            self._n_diameter = 0.0
        else:
            self._n_diameter = in_diameter
        logging.debug( Wheel.__str__( self ) )

    def __str__( self ):
        """Stringify"""
        return f"Manufacturer: {self.__s_manufacturer} | Diameter: {self._n_diameter} [mm]"


class Vehicle( Wheel ):
    def __init__( self, is_vehicle_manufacturer :str = None, in_num_wheels : Number = None, is_wheel_manufacturer : str = None, in_diameter : Number = None ):
        #Call constructor of father
        #SUPER has the type of Vehicle
        super().__init__( is_wheel_manufacturer, in_diameter ) 
        if is_vehicle_manufacturer is None:
            self._s_manufacturer = "?"
        else:
            self._s_manufacturer = is_vehicle_manufacturer

        if in_num_wheels is None:
            self._n_num_wheels = 0
        else:
            self._n_num_wheels = in_num_wheels

        self._lc_wheel = list()
        for n_index in range(in_num_wheels):
            self._lc_wheel.append( Wheel( is_wheel_manufacturer, in_diameter ) )

        logging.debug( Vehicle().__str__( self ) )

    def __str__( self ):
        if not hasattr(self, "_n_num_wheels" ):
            return "NO _n_num_wheels E"

        if self._n_num_wheels <= 0:
            return f"Manufacturer: {self._s_manufacturer} | Number of Wheels: {self._n_num_wheels} | No Wheels"
        else:
            return f"Manufacturer: {self._s_manufacturer} | Number of Wheels: {self._n_num_wheels} | Wheels: " +Wheel.__str__( self._lc_wheel[0] )

class Ev( Vehicle ):
    def __init__( self, in_battery_capacity : Number = None, *args):
        #Call constructor of father
        print(args)
        #SUPER has the type of Vehicle
        super().__init__( args ) 
        if in_battery_capacity is None:
            self._n_battery_capacity = 0.0
        else:
            self._n_battery_capacity = in_battery_capacity

        logging.debug( Ev().__str__( self ) )

    def __str__( self ):
        if not hasattr(self, "_n_num_wheels" ):
            return "NO _n_num_wheels E"

        if self._n_num_wheels <= 0:
            return f"Manufacturer: {self._s_manufacturer} | Number of Wheels: {self._n_num_wheels} | No Wheels"
        else:
            return f"Battery Capacity: {self._n_battery_capacity}  | Vehicle: " +Vehicle.__str__( self )


if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    #my_wheel = Wheel()
    #my_pirellu = Wheel( "Pirelli", 600.0 )

    
    #my_ferrari = Vehicle( "Ferrari", 4, "Pirelli", 450.0 )
    #my_pegeut = Vehicle( "Pegeut", 4, "Donut", 550.0 )

    my_tesla = Ev( 100.0, "Tesla", 3, "Rubby", 350.0 )

    #my_car = Vehicle()

