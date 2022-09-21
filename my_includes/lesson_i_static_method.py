from xmlrpc.client import Boolean


from tokenize import Number
import logging

class Airplane:
    def __init__(self):
        pass

    @staticmethod
    def my_static_method( in_shaka : Number ) -> Boolean:
        logging.debug( f"Number: {in_shaka}" )
        return False

    def my_method( self, in_shaka : Number ) -> Boolean:
        logging.debug( f"Number: {in_shaka}" )
        return False


if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    #static methods have no need for self.
    Airplane.my_static_method( 10.0 )

    Airplane.my_method( Airplane(), 10.0 )