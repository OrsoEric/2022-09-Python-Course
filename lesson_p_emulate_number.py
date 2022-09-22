import logging
import numbers
import warnings
import cmath

class Free_vector:
    """free vector in many dimensions"""
    def __init__( self, in_num_dimensions : numbers.Number = None, it_data = None ) -> None:
        if (in_num_dimensions is None):
            self._n_num_dimensions = 0
            self._vector = list()
        elif (it_data is None):
            self._n_num_dimensions = in_num_dimensions
            self._vector = list( 0 for _ in range(self._n_num_dimensions) )
            logging.debug(f"Construct Dimensions: {self._n_num_dimensions}")
        else:
            self._n_num_dimensions = in_num_dimensions
            self._vector = list( it_data )
        
    def __str__( self ):
        """Stringfy the vector"""
        s_ret = f"Num Dimensions: {self._n_num_dimensions}"
        if (len(self._vector) <= 0):
            return s_ret
        else:
            s_ret += " Content |"
            for n_dimension_index in range( len(self._vector) ):
                s_ret += f" {self._vector[n_dimension_index]} |"

            return s_ret

    def __len__( self ) -> numbers.Number:
        assert len(self._vector) == self._n_num_dimensions, f"Inconsistent dimensions {len(self._vector)} { self._n_num_dimensions}"
        return self._n_num_dimensions

    def __add__( self, ic_rhs ):
        """Overload '+'' operator for this class with this class"""
        assert len(self) == len(ic_rhs), f"Trying sum with vectors of different length {len(self)} { len(ic_rhs)}"

        tn__result = tuple(a+b for a,b in zip(self._vector, ic_rhs._vector))
        logging.debug(f"{tn__result}") 
        return Free_vector( self._n_num_dimensions, tn__result )

    def __neg__(self):
        """Unary minus operator '-'"""
        return Free_vector( self._n_num_dimensions, tuple(-n_value for n_value in self._vector) )

    def __sub__( self, ic_rhs ):
        """Overload '-' operator for this class with this class. use neg operator"""
        return self + (-ic_rhs)

    def __mul__( self, n_scalar ):
        """Overload '*' by constant with constant as right hand side"""
        assert isinstance( n_scalar, numbers.Number ), f"Mul by scalar is getting a non scalar"
        return Free_vector( self._n_num_dimensions, tuple( n_value*n_scalar for n_value in self._vector)  )

    def __rmul__( self, n_scalar ):
        """Overload '*' by constant with constant as left hand side"""
        return self *n_scalar

    def __truediv__( self, n_scalar ):
        """Overload division by scalar"""
        return Free_vector( self._n_num_dimensions, tuple( n_value/n_scalar for n_value in self._vector)  )

    def __matmul__( self, ic_rhs ):
        """Overload '@' by constant with constant as right hand side"""
        warnings.warn( "This is DOT product, should be CROSS product", stacklevel=2 )
        warnings.warn( "This is DOT product, should be CROSS product", stacklevel=1 )
        warnings.warn( "This is DOT product, should be CROSS product", stacklevel=0 )
        return Free_vector( self._n_num_dimensions, tuple(a*b for a,b in zip(self._vector, ic_rhs._vector)) )

    def __abs__( self ):
        """Compute the modulus of the vector"""
        #use a generator
        return cmath.sqrt( sum( n_value**2 for n_value in self._vector ) )

    def __bool__(self):
        """Propagate the bool of the vector"""
        return bool(self._vector)

if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    my_origin = Free_vector( 3 )
    logging.debug( my_origin )

    my_vector_a = Free_vector( 3, (10,11,-7) )
    logging.debug( my_vector_a )

    my_vector_b = Free_vector( 3, (-7,1,-1) )
    logging.debug( my_vector_b )

    my_2d_vector = Free_vector( 2, (10, 10) )
    logging.debug( my_2d_vector )

    logging.debug( f"Sum: {my_vector_a + my_vector_b}" )
    try:
        logging.debug( f"3D +2D Sum: {my_vector_a + my_2d_vector}" )
    except:
        logging.debug( f"Failed to do sum 3D +2D" )

    logging.debug( f"Neg: {-my_vector_b}" )

    logging.debug( f"Sub: {my_vector_a -my_vector_b}" )

    logging.debug( f"Mul by Right Scalar: {my_vector_a * 5}" )
    logging.debug( f"Mul by Left Scalar: {5 * my_vector_a}" )

    try:
        logging.debug( f"Mul with at operator: {my_vector_a * my_vector_b}" )
    except:
        logging.debug("Failed to mul vect by vect with *")

    logging.debug( f"Mul with at operator @: {my_vector_a @ my_vector_b}" )
    
    logging.debug( f"Norm of 2D vector: {abs( my_2d_vector)}" )
    logging.debug( f"Norm of 3D vector: {abs( my_vector_a)}" )
    
    logging.debug( f"Div: {my_vector_a /5}" )

    logging.debug( f"Div: {bool(my_vector_a)}" )


