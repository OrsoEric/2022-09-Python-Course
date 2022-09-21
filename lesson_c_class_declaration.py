class Beer:
    pass

#inherit from beer
class Ale( Beer ):
    pass

#inherit from beer
class Lager( Beer ):
    pass


    #def __init__( self ):

#   if interpreter has the intent of executing this file
if __name__ == "__main__":
    c_nastro_azzurro = Ale()
    #object is the super father
    print( isinstance( c_nastro_azzurro, object ))
    #base class
    print( isinstance( c_nastro_azzurro, Beer ))
    #derived classes
    print( isinstance( c_nastro_azzurro, Ale ))
    print( isinstance( c_nastro_azzurro, Lager ))

    print( "Items inside the class.", dir( Beer() ) )
    print(Beer.__class__)
    print(Beer.__dir__)
    #Dictionary of methods and properties
    print("Dictionary", Beer.__dict__)


    print( "Items inside the instance", dir( c_nastro_azzurro ) )
    