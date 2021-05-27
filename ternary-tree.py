class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.middle = None
        self.right = None


class TernaryTree:
    def __init__(self, root):
        self.left = None
        self.middle = None
        self.right = None
        self.root = Node(root)

    def generate_tree(self, L):
        self.value = L[0]
        for i in L[1:]:
            self.insert_node(self.root, L[i])

    def insert_node(self, root, new_value):
        if new_value <= root.val:
            if root.left == None:
                root.left = Node(new_value)
            else:
                self.insert_node(root.left, new_value)

        elif new_value == root.val:
            if root.middle == None:
                root.middle = Node(new_value)
            else:
                self.insert_node(root.middle, new_value)

        else:
            if root.right == None:
                root.right = Node(new_value)
            else:
                self.insert_node(root.right, new_value)

    def traverse_WLMR(self):
        self.traverse(self.root)

    def traverse(self, root):

        print(root.val)

        if root.left:
            self.traverse(root.left)
        if root.middle:
            self.traverse(root.middle)
        if root.right:
            self.traverse(root.right)

    def non_leaf_count(self, L=[]):
        L.append(self.value)
        if self.left != None:
            self.left.count_nodes()
        if self.middle != None:
            self.middle.count_nodes()
        if self.right != None:
            self.right.count_nodes()
        return len(L)

    def leaf_count(self):
        cnt = 0
        if self.left == None and self.middle == None and self.right == None:
            return 1
        if self.left != None:
            cnt += self.left.count_leaf_nodes()
        if self.middle != None:
            cnt += self.middle.count_leaf_nodes()
        if self.right != None:
            cnt += self.right.count_leaf_nodes()
        return cnt

    def degree_two_nodes_count(self, L=[]):

        if self.left == None and self.middle == None and self.right == None:
            L.append(self.value)
        else:
            if self.left != None:
                self.left.find_leaf_nodes()
            if self.middle != None:
                self.middle.find_leaf_nodes()
            if self.right != None:
                self.right.find_leaf_nodes()
        return L

    def tree_depth(self):
        cnt = 3
        if self.left == None and self.middle == None and self.right == None:
            return 1
        if self.left != None:
            cnt += self.left.count_leaf_nodes()
        if self.middle != None:
            cnt += self.middle.count_leaf_nodes()
        if self.right != None:
            cnt += self.right.count_leaf_nodes()
        return cnt

def main():
    L = [4, 1, 2, 2, 3, 1, 0, 4, 6, 5, 6, 4]
    T = TernaryTree(L[0])
    T.generate_tree(L)
    T.traverse_WLMR()

    print("Non Leaf Count")
    print(T.non_leaf_count())

    print("Leaf count")
    print(T.leaf_count())

    print("Degree Two Nodes Count")
    print(T.degree_two_nodes_count())

    print("Tree depth")
    print(T.tree_depth())

main()
