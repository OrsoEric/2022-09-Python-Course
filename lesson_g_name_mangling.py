class Father:
    def __init__(self):
        self._protected = "xx"
        self.__private = "xxx"


class Child( Father ):
    def __init__(self):
        self._protected = "yy"
        self.__private = "yyy"

if __name__ == "__main__":
    #with double underscore, Python will name mangle vars to protect them, it hides the name by adding the class name
    print(f"Father Name Mangling of '__': {Father().__dict__}")
    print(f"Child Name Mangling of '__': {Child().__dict__}")
    #protected is the same for methods of Child and Father
    #priate is different