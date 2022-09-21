#name for vars, verbs for methods

class Beer:
    """My beer father class"""
    
    def __init__( self, is_country=None ):
        """Empty Constructor
        Args:
            is_country | name of the country, I have a parameter that can be skipped
        self | is an user defined name for the pointer to the class memory
        init | takes care of declaring the class vars
        what I add is inside the dictionary, this is why I can add and edit at any point
        
        """
        #check if the value was specified
        if is_country is None:
            #_is because it's a variable inside a class
            self._s_country = "?"
        print(f"Init of {self.__class__} | Dict {self.__dict__}" )
        
        return

    #Getters and Setters are mapped to the same name using property
    @property
    def country( self ):
        """Getter for _s_country
        in python there are no getters and setter. Python use properties
        It's not inside dictionary"""
        print(f"Get self._country: {self._s_country}")
        return self._s_country
    @country.setter
    def country( self, is_country : str() ):
        """Setter and getter maps to the same property that modify
        Args:
            is_country: country name
        """
        print(f"Set self._s_country: {is_country}")
        self._s_country = is_country


#inherit from beer
class Ale( Beer ):
    pass

#inherit from beer
class Lager( Beer ):
    pass


    #


#   if interpreter has the intent of executing this file
if __name__ == "__main__":
    c_nastro_azzurro = Ale()
    #object is the super father
    print( isinstance( c_nastro_azzurro, object ))
    #base class
    print( isinstance( c_nastro_azzurro, Beer ))
    print( f"Docstring in a class is executed and can be read | {Beer.__doc__}")
    #derived classes
    print( isinstance( c_nastro_azzurro, Ale ))
    print( isinstance( c_nastro_azzurro, Lager ))


    print( f"Country property: {c_nastro_azzurro.country} " )
    c_nastro_azzurro.country = "Italy"
    
