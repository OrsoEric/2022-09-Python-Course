import logging
import numbers

#find the nth fibonacci number overloading bracket operator

class Fibonacci:
    def __init__( self ):
        #cache previously computed 
        self._d_cache = dict()

    def __getitem__( self, key : numbers.Number ) -> numbers.Number:
        if key in self._d_cache:
            logging.debug( f"Cached {key}")
            return self._d_cache[key]
        else:

            a = 0
            b = 1
            y = 0
            if (key == 0):
                self._d_cache[key] = 0
                return 0
            elif (key == 1):
                self._d_cache[key] = 1
                return 1
            else:
                for n_index in range(key-1):
                    y = a + b
                    a = b
                    b = y
                    self._d_cache[key] = y
                return y

    def __call__( self, value : numbers.Number ) -> numbers.Number:
        return self[value]


if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    my_fibonacci = Fibonacci()

    for n_index in range( 10 ):
        logging.debug( f" {n_index} -> {my_fibonacci[n_index] }" )

    for n_index in range( 10 ):
        logging.debug( f" {n_index} -> {my_fibonacci(n_index) }" )
