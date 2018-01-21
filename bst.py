class node:
    def __init__(self, value=None):
        self.value = value
        self.left_node = None
        self.right_node = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            #This is a private function we need to use for recursive calls            
            self._insert(value, self.root)

    def _insert(self, value, cur_node):

        #First scenario, if value is less that root value
        if value < cur_node.value:

            # Two scenarios: current node has a left child. Or Not.

            if cur_node.left_child == None:
                # We need to create a left child since None exist currently
                cur_node.left_node = node(value)
            else:
                #If there is already a left node, we need to find a place to
                # add this value else where (until we find a node with no left_node
                #Hence we call _insert function again with cur_node
                # as cur_node.left_node. This recurtion will end when a None is found
                #i.e a node with no left_node
                self._insert(value, cur_node.left_node)
                
            
