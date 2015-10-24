class RedBlackNode(object):
    def __init__(self, value, parentnode = None):
        self.value = value
        self.parent = parentnode
        self.left = None
        self.right = None
        self.red = parentnode is not None
        self.fix_tree()

    def find(self, value):
        if self.value == value:
            return self
        elif value < self.value and self.left is not None:
            return self.left.find(value)
        elif self.right is not None:
            return self.right.find(value)
        else:
            return None


    def get_root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.get_root()

    def print_tree(self, numindent=0):
        if numindent == 0:
            print '--------------------------------------------------------------------------------'
        if self.right is not None:
            self.right.print_tree(numindent+1)
        print('{}{} {}'.format('\t'*numindent, self.value, 'Red' if self.red else 'Black'))
        if self.left is not None:
            self.left.print_tree(numindent+1)

    def set_root_black(self):
        if self.parent is None:
            self.red = False
        else:
            self.parent.set_root_black()

    def is_uncle_red(self):
        if self.get_grand_parent() is None:
            return False
        elif self.is_parent_left_child():
            return self.get_grand_parent().right is not None and self.get_grand_parent().right.red
        else:
            return self.get_grand_parent().left is not None and self.get_grand_parent().left.red

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
            tempright = self.left.right
            templeft = self.left
            tempparent = self.parent
            self.left.right = self
            self.left.parent = tempparent
            self.left = tempright
            self.parent = templeft
            if tempparent is not None:
                if tempparent.left == self:
                    tempparent.left = templeft
                else:
                    tempparent.right = templeft

    def rotate_left(self):
        if self.right is not None:
            templeft = self.right.left
            tempright = self.right
            tempparent = self.parent
            self.right.left = self
            self.right.parent = tempparent
            self.right = templeft
            self.parent = tempright

            if tempparent is not None:
                if tempparent.left == self:
                    tempparent.left = tempright
                else:
                    tempparent.right = tempright


    def insert(self, value):

        if self.value < value:
            if self.right is None:
                self.right = RedBlackNode(value, self)
            else:
                self.right.insert(value)

        else:
            if self.left is None:
                self.left = RedBlackNode(value, self)
            else:
                self.left.insert(value)

    def is_parent_left_child(self):
        return self.parent == self.get_grand_parent().left

    def is_parent_right_child(self):
        return not self.is_parent_left_child()

    def fix_tree(self):
        if self.get_grand_parent() is not None and self.parent is not None and self.red and self.parent.red:
            if self.is_uncle_red(): #CASE 1
                self.parent.red = False
                if self.get_uncle() is not None:
                    self.get_uncle().red = False
                self.get_grand_parent().red = True
                self.get_grand_parent().fix_tree()
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



if __name__ == '__main__':
    root = RedBlackNode(10)

    root.get_root().insert(9)
    root.get_root().insert(8)
    root.get_root().insert(7)
    root.get_root().insert(6)
    root.get_root().insert(5)
    root.get_root().insert(4)
    root.get_root().insert(3)
    root.get_root().insert(2)

    root.get_root().insert(1)

    root.get_root().print_tree()
    root.get_root().insert(11)
    root.get_root().print_tree()

