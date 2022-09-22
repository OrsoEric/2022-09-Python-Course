import logging

#find the nth fibonacci number overloading bracket operator

class Fibonacci:
    def __init__( self ):
        pass

    def __getitem__( self, key ):
        a = 0
        b = 1
        y = 0
        if (key == 0):
            return 0
        elif (key == 1):
            return 1
        else:
            for n_index in range(key-1):
                y = a + b
                a = b
                b = y
            return y





if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    my_fibonacci = Fibonacci()

    for n_index in range( 10 ):
        logging.debug( f" {n_index} -> {my_fibonacci[n_index] }" )
