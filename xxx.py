import numbers
from tokenize import Number

#import dataclasses
#@dataclasses

class Jack:
    def __init__(self, in_x = 0, in_y = 0 ) -> None:
        self.x = in_x
        self._y = in_y

    def shaka(self) -> float:
        return self.x +self._y +1

if __name__ == "__main__":
    my_friend = Jack()
    print( my_friend.x )
    my_friend.x+=1
    print( my_friend.x )
    print( my_friend._y )
