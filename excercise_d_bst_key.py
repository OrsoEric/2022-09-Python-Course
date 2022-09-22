import logging
from numbers import Number

class Node:
    def __init__( self, i_key = None, i_value=None ) -> None:
        """Construct a node with a Key and a value"""
        self._key = i_key
        self._value = i_value
        self._father = None
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
    def father( self ):
        """getter _father"""
        return self._father

    @father.setter
    def father( self, i_father : "Node" ) -> bool:
        """setter _father"""
        self._father = i_father
        return False

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

    def add(self, i_key, i_value ) -> Node:
        """Add a new node to the tree"""
        #contruct a new node
        new_node = Node( i_key, i_value )
        #traverse from root
        current_node = self._root
        while (current_node is not None):
            if (new_node == current_node):
                #there can't be two nodes with same keys
                logging.error(f"Trying to add node with same key {new_node.key} as existing node {current_node.key}")
                return None
            elif (new_node < current_node):
                if (current_node.left is None):
                    current_node.left = new_node
                    new_node.father = current_node
                else:
                    current_node = current_node.left
            elif (new_node > current_node):
                if (current_node.right is None):
                    current_node.right = new_node
                    new_node.father = current_node
                else:
                    current_node = current_node.right
            else:
                raise Exception(f"Algorithmic error. Key {new_node.key} is neither < == nor > as  {current_node.key}")
        else:
            self._root = new_node
            new_node.father = None
        return new_node

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
                raise Exception(f"Algorithmic error. Key {i_key} is neither '<' '==' nor '>' as  {current_node.key}")
        else:
            return None

    def successor( self, i_node : Node = None):
        """Find the smallest node that is bigger than the given node"""

        if (i_node is None):
            return None
        #if I have a > child, go to major, and go as left as possible
        if (i_node.right is not None):
            i_node = i_node.right
            while (i_node.left is not None):
                i_node = i_node.left
            return i_node
        #I don't have a > child. I need to go up, and go down if I'm not already a <
        elif (i_node.father is not None):
            #go up, remember key
            i_key = i_node.key
            i_node = i_node.father
            #while I'm the left child of the father, I found the successor
            while (i_key > i_node.key):
                #if node has a father
                if (i_node.father is not None):
                    i_key = i_node.key
                    i_node = i_node.father
                #I reached the root
                else:
                    return None
                    raise Exception(f"Root")
            else:
                return i_node
        #I can't go up if I'm the root, I dont' have a successor
        else:
            return None

    def node_iterator( self, start_key, stop_key ):
        """Iterate nodes from start key to stop key"""
        node = self.find_node( start_key )
        if (node is None):
            return None
        while (node.key <= stop_key):
            yield node
            node = self.successor( node )

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
        if (current_node.father is None):
            s_print = f"{current_node.key} | {current_node.value}"
        else:
            s_print = f"{current_node.key} ({current_node.father.key}) | {current_node.value} | "
        #print the node
        print( is_indent + is_branch + s_print )
        if (current_node.left is not None):
            self.show( current_node.left, is_indent +"    ", is_branch="< | " )
        if (current_node.right is not None):
            self.show( current_node.right, is_indent+"    ", is_branch="> | " )
            
    def __getitem__( self, i_key ):
        """Find an item with a given key"""
        #when key is a number
        if (isinstance(i_key,Number)):
            return self.find_node( i_key )
        #when key is a slice
        elif (isinstance(i_key, slice)):
            assert i_key is not None, "Step not supported"
            return [str(x) for x in self.node_iterator( i_key.start, i_key.stop )]
        else:
            raise Exception("Not implemented yet")
        
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
    #my_node = Node( 42, "Erd Tree Root" )
    #print("Key: ", my_node.key)
    my_tree = Binary_search_tree()
    if (False):
        print( my_tree )
        my_tree.add( 42, "Erd Tree Root" )
        node_search = my_tree.add( 40, "Lurnia" )
        my_tree.add( 999, "Elden Nord" )
        my_tree.add( 44, "Caelid" )
        my_tree.add( 43, "Sellen" )
        my_tree.add( 45, "Luden" )
        my_tree.add( 41, "Troy" )
        my_tree.add( 999, "Elden Lady" )

    my_tree.add( 2, "*" )
    my_tree.add( 1, "*" )
    my_tree.add( 33, "*" )
    my_tree.add( 25, "*" )
    my_tree.add( 0, "*" )
    my_tree.add( 40, "*" )
    my_tree.add( 11, "*" )
    my_tree.add( 34, "*" )
    my_tree.add( 7, "*" )
    my_tree.add( 12, "*" )
    my_tree.add( 36, "*" )
    my_tree.add( 13, "*" )
    my_tree.show()

    print( "--------------------------------------------------" )

    if (True):
        #right
        print( "Successor: ", my_tree.successor( my_tree.find_node(2) ) )
        print( "Successor: ", my_tree.successor( my_tree.find_node(11) ) )
        print( "Successor: ", my_tree.successor( my_tree.find_node(12) ) )

        #father
        print( "Successor: ", my_tree.successor( my_tree.find_node(1) ) )
        print( "Successor: ", my_tree.successor( my_tree.find_node(7) ) )

        print( "Successor: 13 -> ", my_tree.successor( my_tree.find_node(13) ) )
        print( "Successor: 25 -> ", my_tree.successor( my_tree.find_node(25) ) )
        print( "Successor: 40 -> ", my_tree.successor( my_tree.find_node(40) ) )

        print( "Successor: 36 -> ", my_tree.successor( my_tree.find_node(36) ) )
        print( "Successor: 34 -> ", my_tree.successor( my_tree.find_node(34) ) )


    print( "--------------------------------------------------" )
    


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

    if (True):
        print( "--------------------------------------------------" )
        print("Test an iterator that returns all nodes in a given range")
        print( [x.__str__() for x in my_tree.node_iterator(7, 25) ])

    if (True):
        print( "--------------------------------------------------" )
        print("Test item index with overload of square bracket operator")
        print( my_tree[7] )

    if (True):
        print( "--------------------------------------------------" )
        print("Test slice")
        print( my_tree[7:25] )