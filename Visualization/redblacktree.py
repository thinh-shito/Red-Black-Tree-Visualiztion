# Implementing Red-Black Tree in Python


import sys

radius = 20
canvas_width = 1600
canvas_height = 970
mid_canvas_width = canvas_width // 2
mid_canvas_height = canvas_height // 2


# Node creation
class Node:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.pos = [0, 0]
        self.color = 1


class coord:
    key = 0
    pos0 = [0, 0]
    pos1 = [0, 0]
    color = 0
    side = 'm'

    def __init__(self, pos0, pos1, color, key, side='m'):
        self.pos0 = pos0
        self.pos1 = pos1
        self.color = color
        self.key = key
        self.side = side

    def get(self):
        return self.pos0, self.pos1

    def get_key(self):
        return self.key

    def equal(self, other):
        return self.pos0 == other.pos0 and self.pos1 == other.pos1 and self.color == other.color and self.key == other.key and self.side == other.side


class RedBlackTree:
    def __init__(self):
        self.NULL = Node(0)
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.NULL.pos = [0, 0]
        self.root = self.NULL
        self.forest = []

    # Preorder
    def pre_order_helper(self, node):
        if node != self.NULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder
    def in_order_helper(self, node):
        if node != self.NULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    # Postorder
    def post_order_helper(self, node):
        if node != self.NULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    # Search the tree
    def search_tree_helper(self, node, key):
        if node == self.NULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    # s.color = 0
                    # x.parent.color = 1
                    t1 = s
                    t2 = x.parent
                    self.left_rotate(x.parent)
                    self.forest.append(self.get_coordinates())
                    t1.color = 0
                    t2.color = 1
                    s = x.parent.right
                    self.forest.append(self.get_coordinates())


                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                    self.forest.append(self.get_coordinates())
                else:
                    if s.right.color == 0:
                        # s.left.color = 0
                        # s.color = 1
                        t1 = s.left
                        t2 = s
                        self.right_rotate(s)
                        self.forest.append(self.get_coordinates())
                        t1.color = 0
                        t2.color = 1
                        s = x.parent.right
                        self.forest.append(self.get_coordinates())
                    s.color = x.parent.color
                    # x.parent.color = 0
                    # s.right.color = 0
                    t1 = x.parent
                    t2 = s.right
                    self.left_rotate(x.parent)
                    t1.parent.color = 0
                    self.forest.append(self.get_coordinates())
                    t1.parent.color = 1
                    t1.color = 0
                    t2.color = 0
                    x = self.root
                    self.forest.append(self.get_coordinates())
            else:
                s = x.parent.left
                if s.color == 1:
                    # s.color = 0
                    # x.parent.color = 1
                    t1 = s
                    t2 = x.parent
                    self.right_rotate(x.parent)
                    self.forest.append(self.get_coordinates())
                    t1.color = 0
                    t2.color = 1
                    s = x.parent.left
                    self.forest.append(self.get_coordinates())

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                    self.forest.append(self.get_coordinates())
                else:
                    if s.left.color == 0:
                        # s.right.color = 0
                        # s.color = 1
                        t1 = s.right
                        t2 = s
                        self.left_rotate(s)
                        self.forest.append(self.get_coordinates())
                        t1.color = 0
                        t2.color = 1
                        s = x.parent.left
                        self.forest.append(self.get_coordinates())
                    # left left rotation
                    s.color = x.parent.color
                    # x.parent.color = 0
                    # s.left.color = 0
                    t1 = x.parent
                    t2 = s.left
                    self.right_rotate(x.parent)
                    t1.parent.color = 0
                    self.forest.append(self.get_coordinates())
                    t1.parent.color = 1
                    t1.color = 0
                    t2.color = 0
                    x = self.root
                    self.forest.append(self.get_coordinates())
        if x.color == 1:
            x.color = 0
            self.forest.append(self.get_coordinates())


    def __rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self, node, key):
        z = self.NULL
        while node != self.NULL:
            if node.item == key:
                z = node

            if node.item < key:
                node = node.right
            else:
                node = node.left

        if z == self.NULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)

                y.right = z.right
                y.right.parent = y
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        self.forest.append(self.get_coordinates())
        if y_original_color == 0:
            self.delete_fix(x)
            self.forest.append(self.get_coordinates())

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                        self.forest.append(self.get_coordinates())
                    t1 = k.parent
                    t2 = k.parent.parent
                    self.left_rotate(k.parent.parent)
                    self.forest.append(self.get_coordinates())
                    t1.color = 0
                    t2.color = 1
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                        self.forest.append(self.get_coordinates())
                    t1 = k.parent
                    t2 = k.parent.parent
                    self.right_rotate(k.parent.parent)
                    self.forest.append(self.get_coordinates())
                    t1.color = 0
                    t2.color = 1
            self.forest.append(self.get_coordinates())
            if k == self.root:
                break
        if self.root.color == 1:
            self.root.color = 0
            self.forest.append(self.get_coordinates())

    # Printing the tree
    def __print_helper(self, node, indent, last):
        if node != self.NULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.NULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.NULL and x == y.right:
            x = y
            y = y.parent

        return y

    def predecessor(self, x):
        if x.left != self.NULL:
            return self.maximum(x.left)

        y = x.parent
        while y != self.NULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x


        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x


        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        n = self.searchTree(key)
        if n.item == key:
            return
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node
        self.forest.append(self.get_coordinates())
        if node.parent is None:
            node.color = 0
            self.forest.append(self.get_coordinates())
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.delete_node_helper(self.root, item)

    def print_tree(self):
        self.__print_helper(self.root, "", True)

    def list_key(self, node, keys=None):
        if keys is None:
            keys = []
        if node != self.NULL:
            self.list_key(node.left, keys)
            keys.append(node.item)
            self.list_key(node.right, keys)

    def get_list_key(self):
        keys = []
        self.list_key(self.root, keys)
        return keys

    def coordinates(self, nodes):
        list_coords = nodes
        root = self.root  # start with root of the tree
        # Place root node at position tree.pos
        if root.item != 0:
            root_coord = [mid_canvas_width, 60]
            root.pos = root_coord
            node1 = coord(root_coord, root_coord, root.color, root.item)
            list_coords.append(node1)

            # Recursively place the other nodes and edges
            def add_nodes(node, gap, nodes, coords):
                if node.left and node.left.item != 0:  # if left subtree: position node to left of parent
                    new_coord = [coords[0] - gap, coords[1] + 4 * radius]
                    node.left.pos = new_coord
                    node2 = coord(coords, new_coord, node.left.color, node.left.item, 'l')
                    nodes.append(node2)
                    # recurse on left subtree
                    add_nodes(node.left, gap // 2, nodes, new_coord)

                if node.right and node.right.item != 0:  # if right subtree: position node to right of parent
                    new_coord = [coords[0] + gap, coords[1] + 4 * radius]
                    node.right.pos = new_coord
                    node3 = coord(coords, new_coord, node.right.color, node.right.item, 'r')
                    nodes.append(node3)
                    # recurse on right subtree
                    add_nodes(node.right, gap // 2, nodes, new_coord)

            add_nodes(self.root, 18 * radius, list_coords, root_coord)
        return list_coords

    def get_coordinates(self):
        return self.coordinates([])

    def get_forest(self):

        return self.forest


if __name__ == "__main__":
    bst = RedBlackTree()

    keys = ['13', '9', '5']
    # for i in keys:
    #     bst.insert(int(i))
    #     node = bst.get_coordinates()
    #     for j in node:
    #         print(j.key, j.get())
    #     print('\n')
    # bst.insert(60)
    # bst.insert(75)
    # bst.insert(57)

    # bst.print_tree()
