class RedBlackNode(object):
    def __init__(self, parentnode, value):
        self.value = value
        self.parent = parentnode
        self.left = None
        self.right = None
        self.red = parentnode is not None
        self.fix_tree()


    def set_root_black(self):
        if self.parent is None:
            self.red = False
        else:
            self.parent.set_root_black()

    def get_uncle(self):
        if self.get_grand_parent() is None:
            return None
        elif self.is_parent_left_child():
            return self.get_grand_parent().right
        else:
            return self.get_grand_parent().left



    def get_grand_parent(self):
        if self.parent is not None:
            return self.parent.parent

        return None

    def rotate_right(self):
        if self.left is not None:
            self.left.right, self.left, self.parent, self.left.parent = self, self.left.right, self.left, self.parent

    def rotate_left(self):
        if self.right is not None:
            self.right.left, self.right, self.parent, self.right.parent = self, self.right.left, self.right, self.parent

    def insert(self, value):
        if self.value < value:
            if self.right is None:
                self.right = RedBlackNode(self, value)
            else:
                self.right.insert(value)

        else:
            if self.left is None:
                self.left = RedBlackNode(self, value)
            else:
                self.right.insert(value)

    def is_parent_left_child(self):
        return self.parent == self.get_grand_parent().left

    def is_parent_right_child(self):
        return not self.is_parent_left_child()

    def fix_tree(self):
        if self.parent is not None and self.red:
            if self.get_uncle() is not None and self.get_uncle().red: #CASE 1
                self.parent.red = False
                self.get_uncle().red = False
                self.get_grand_parent().red = True
                self.get_grand_parent().fixTree()
            elif self.is_parent_left_child():
                if self == self.parent.right:
                    self.parent.rotate_left()
                self.parent.red = False
                self.get_grand_parent().red = True
                self.get_grand_parent().rotate_right()
            else:
                if self == self.parent.left:
                    self.parent.rotate_right()

                self.parent.red = False
                self.get_grand_parent().red = True
                self.get_grand_parent().rotate_left()


        self.set_root_black()
