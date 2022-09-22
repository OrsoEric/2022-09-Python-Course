#I have a container, a method to get the iterator and a next to jump
#automatically called by generators and list comprheension
#raise stop iteration exception when done

import logging
import numbers

from itertools import  product

#find the nth fibonacci number overloading bracket operator
class Turnip:
    def __init__( self ):
        """Allocate a dummy thing to iterate on"""
        self._ln_list = list( (4, 8, 15, 16, 23, 42) )

    def __iter__( self ):
        """Construct an iterator, must return itself"""
        class My_iterator():
            """Declare iterator class to hold my indexes and references to the data. It can inherit the father"""
            def __init__( self, iln_data ):
                self._n_index = 0
                self._ln_data = iln_data
            def __iter__( self ):
                """Sugar"""
                return self
            def __next__( self ):
                """Next element. Raises StopIteration to let 'for' know when it's done. Return what the iterator should return"""
                if (self._n_index >= len( self._ln_data )):
                    raise StopIteration
                else:   
                    self._n_index += 1
                    return self._ln_data[self._n_index -1]
        return My_iterator( self._ln_list )


    


if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    for xxx in Turnip():
        logging.debug( f"{xxx}" )

    for x,y in product( Turnip(), Turnip() ):
        logging.debug(f" {x} {y} ")
