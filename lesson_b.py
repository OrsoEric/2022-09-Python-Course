import numbers
import fractions
import math
import cmath

def what_is_the_type_of( n_number ):
    """AI is creating summary for what_is_the_type_of
    Args:
        n_number ([type]): [description]
    Returns:
        False = OK | True = FAIL
    """
    if isinstance( n_number, numbers.Number ):
        s_res = "Number"
        print( f"Type of number {n_number}  is: {s_res}")
    if isinstance( n_number, numbers.Integral ):
        s_res = "Integral"
        print( f"Type of number {n_number}  is: {s_res}")
    if isinstance( n_number, numbers.Rational ):
        s_res = "Rational"
        print( f"Type of number {n_number}  is: {s_res}")
    if isinstance( n_number, numbers.Real ):
        s_res = "Real"
        print( f"Type of number {n_number}  is: {s_res}")
    if isinstance( n_number, numbers.Complex ):
        s_res = "Complex"
        print( f"Type of number {n_number}  is: {s_res}")
    #else:
    #    s_res = "Unknown"
    #    return True
    
    return False

#--------------------------------------------------------------------------------------------------------------------------------
#   MAIN
#--------------------------------------------------------------------------------------------------------------------------------

#   if interpreter has the intent of executing this file
if __name__ == "__main__":

    what_is_the_type_of( 3.3 )
    what_is_the_type_of( 3 )
    what_is_the_type_of( 5/2 )
    what_is_the_type_of( fractions.Fraction(5, 2) )
    what_is_the_type_of( math.sqrt( 9.0 ) )
    what_is_the_type_of( cmath.sqrt( -9.0 ) )

