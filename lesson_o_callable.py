import numbers
import logging

class Shaka:
    def __init__(self):
        self._ln_payload = list(range(10))


        self._d_ledger = dict()



    def __len__(self):
        """Return the length of the class"""
        return len( self._ln_payload )

    def __call__( self, in_num : numbers.Number ):
        """Turn an object into a callable. FUNCTOR"""
        return in_num

    def __getitem__( self, key ):
        """Allow use of bracket operator for getter"""
        return self._d_ledger[ key ]

    def __setitem__( self, key, value ):
        """Overloads bracket assignment operator as LHS"""
        self._d_ledger[ key ] = value
        logging.debug(f"Entry {key} set {self._d_ledger[ key ]}")

    def __missing__( self, key ):
        """Handle missing items"""
        logging.debug(f"Missing {key}")
        

    def __del_item__( self, key ):
        pass

    


    def __contain__( self ):
        """overload >>>>in<<<< operator"""
        pass

    def __iter__(self):
        """Iterator allow to get elements one after the other, can be multidimensional"""
        return


    def __reversed__(self):
        """Return the reversed structure, phyton does it automatically if it has indexes?"""
        pass


if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    c_test = Shaka()
    logging.debug( f"Turn into callable: {c_test( 10 )}",  )
    
    #logging.debug( "Overload len(): ", len( c_test ) )

    #logging.debug( "Implement bracket operator: ", c_test[0] )

    c_test[12] = 10
    logging.debug( f"Test Set {c_test[12]}" )
    logging.debug( f"Test Missing {c_test[13]}" )