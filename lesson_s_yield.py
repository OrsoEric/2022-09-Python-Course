import logging
import numbers


def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        y = a + b
        a = b
        b = y

class Onion:
    def __init__( self ):
        """Allocate a dummy thing to iterate on"""
        self._ln_list = list( (4, 8, 15, 16, 23, 42) )

    def __iter__( self ):
        """I return the iterator of the parent list, it's still a generator"""
        return (x for x in self._ln_list)


if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    logging.debug( [x for x, y in zip( fibonacci(), range(10))] )

    for xxx in Onion():
        logging.debug( f"{xxx}" )