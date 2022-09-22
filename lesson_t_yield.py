import logging
import numbers


class Explore_slice():
    def __getitem__( self, in_index ):
        logging.debug(f"{in_index}")



if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )



    my_class = Explore_slice()
    my_class[0]
    my_class[0:5]
    my_class[0:5:2]