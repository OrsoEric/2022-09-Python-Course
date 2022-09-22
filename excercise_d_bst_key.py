import logging
from numbers import Number

class Node:
    def __init__( self, i_key = None, i_value=None ) -> None:
        """Construct a node with a Key and a value"""
        self._key = i_key
        self._value = i_value
        self._left = None
        self._right = None
        logging.debug(f"Construct Node | {self}")

    @property
    def key( self ):
        """getter _key"""
        return self._key
    
    @property
    def value( self ):
        """getter _value"""
        return self._value

    @property
    def left( self ):
        """getter _left"""
        return self._left

    @left.setter
    def left( self, i_left : "Node" ) -> bool:
        """setter _left"""
        self._left = i_left
        return False

    @property
    def right( self ):
        """getter _right"""
        return self._right

    @right.setter
    def right( self, i_right : "Node" ) -> bool:
        """setter _right"""
        self._right = i_right
        return False

    def __eq__( self, rhs : "Node "):
        """Overload '==' between Node"""
        return (self.key == rhs.key)

    def __lt__( self, rhs : "Node "):
        """Overload '<' between Node"""
        return self.key < rhs.key


    def __str__(self) -> str:
        """Stringfy. Show key, value and ID of three items"""
        return f"Key {self._key} | Value {self._value} | Self: {id(self)} | Left {id(self._left)} | Right {id(self._right)}"

class Binary_search_tree:
    def __init__(self):
        """Empty tree constructor"""
        self._root = None

    def add(self, i_key, i_value ) -> bool:
        """Add a new node to the tree"""
        #contruct a new node
        new_node = Node( i_key, i_value )
        #traverse from root
        current_node = self._root
        while (current_node is not None):
            if (new_node == current_node):
                #there can't be two nodes with same keys
                logging.error(f"Trying to add node with same key {new_node.key} as existing node {current_node.key}")
                return True
            elif (new_node < current_node):
                if (current_node.left is None):
                    current_node.left = new_node
                else:
                    current_node = current_node.left
            elif (new_node > current_node):
                if (current_node.right is None):
                    current_node.right = new_node
                else:
                    current_node = current_node.right
            else:
                raise Exception(f"Algorithmic error. Key {new_node.key} is neither < == nor > as  {current_node.key}")
        else:
            self._root = new_node

    def find_node( self, i_key = None ):
        """Find a node with a given key"""
        if (i_key == None):
            return None
        current_node = self._root
        while (current_node is not None):
            #logging.debug(f"{current_node}")
            if (current_node.key == i_key):
                return current_node
            elif (i_key < current_node.key):
                current_node = current_node.left
            elif (i_key > current_node.key):
                current_node = current_node.right
            else:
                raise Exception(f"Algorithmic error. Key {i_key} is neither < == nor > as  {current_node.key}")
        else:
            return None
    

    def show( self, i_node : Node = None, is_indent : str = "", is_branch : str = None ):
        """Show the tree structure, key and content"""
        if (self._root is None ):
            print( "Empty Tree" )
            return True

        if (i_node is None):
            is_branch = ") | "
            current_node = self._root
        else:
            current_node = i_node

        s_print = f"{current_node.key} | {current_node.value}"
        #print the node
        print( is_indent + is_branch + s_print )
        if (current_node.left is not None):
            self.show( current_node.left, is_indent +"    ", is_branch="< | " )
        if (current_node.right is not None):
            self.show( current_node.right, is_indent+"    ", is_branch="> | " )
            
    def __contains__( self, i_key = None ):
        return (self.find_node( i_key ) is not None)

    def __str__(self):
        """Stringfy the tree"""
        if (self._root is None ):
            return f"None"
        else:
            return Node(self._root).__str__()

if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, format='[%(asctime)s] %(module)s:%(lineno)d %(levelname)s> %(message)s' )

    #my_node = Node()
    my_node = Node( 42, "Erd Tree Root" )
    #print("Key: ", my_node.key)

    my_tree = Binary_search_tree()
    print( my_tree )
    my_tree.add( 42, "Erd Tree Root" )
    my_tree.add( 40, "Lurnia" )
    my_tree.add( 999, "Elden Nord" )
    my_tree.add( 44, "Caelid" )
    my_tree.add( 43, "Sellen" )
    my_tree.add( 45, "Luden" )
    my_tree.add( 41, "Troy" )
    my_tree.add( 999, "Elden Lady" )
    
    print( "--------------------------------------------------" )
    my_tree.show()
    if (False):
        print( "--------------------------------------------------" )
        print("Test find_node")
        print( my_tree.find_node( 42 ) )
        print( my_tree.find_node( 40 ) )
        print( my_tree.find_node( 999 ) )
        print( my_tree.find_node( 404 ) )
        
    if (False):
        print( "--------------------------------------------------" )
        print("Test contains")
        print( 999 in my_tree )
        print( 404 in my_tree )

