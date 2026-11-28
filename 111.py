
# BST USING LINKED LIST

# 1. CREATE NODE
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


# 2. CREATE BST
class BST:
    def __init__(self):
        self.root = None

    # 3. INSERT NODE
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    # 4. SEARCH NODE
    def search(self, key):
        temp = self.root

        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        return False

    # 5. INORDER (LEFT ROOT RIGHT)
    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    # 6. PREORDER (ROOT LEFT RIGHT)
    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    # 7. POSTORDER (LEFT RIGHT ROOT)
    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.data, end=" ")

    # 8. COUNT TOTAL NODES
    def count_nodes(self, rt):
        if rt is None:
            return 0
        return 1 + self.count_nodes(rt.left) + self.count_nodes(rt.right)

    # 9. COUNT LEAF NODES
    def count_leaf(self, rt):
        if rt is None:
            return 0

        if rt.left is None and rt.right is None:
            return 1

        return self.count_leaf(rt.left) + self.count_leaf(rt.right)

    # 10. COUNT NON-LEAF NODES
    def count_nonleaf(self, rt):
        if rt is None:
            return 0

        if rt.left is None and rt.right is None:
            return 0

        return 1 + self.count_nonleaf(rt.left) + self.count_nonleaf(rt.right)

    # 11. FIND MINIMUM AND MAXIMUM
    def findminmax(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root

        while temp.left:
            temp = temp.left
        print("Minimum:", temp.data)

        temp = self.root

        while temp.right:
            temp = temp.right
        print("Maximum:", temp.data)

    # 12. DELETE NODE
    def delete(self, rt, value):
        if rt is None:
            return rt

        if value < rt.data:
            rt.left = self.delete(rt.left, value)

        elif value > rt.data:
            rt.right = self.delete(rt.right, value)

        else:
            # CASE 1: NO LEFT CHILD
            if rt.left is None:
                return rt.right

            # CASE 2: NO RIGHT CHILD
            if rt.right is None:
                return rt.left

            # CASE 3: TWO CHILDREN
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.delete(rt.right, succ.data)

        return rt

    # FIND SUCCESSOR (SMALLEST RIGHT NODE)
    def get_successor(self, temp):
        temp = temp.right

        while temp.left:
            temp = temp.left

        return temp

    # 13. LEVEL ORDER + NEXT LEVEL NODE COUNT
    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return

        arr = [rt]
        cnt = 0
        level = 0

        while cnt < len(arr):

            # COUNT NODES IN CURRENT LEVEL
            node_count = len(arr) - cnt

            print("\nLevel", level, "nodes:", end=" ")

            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1

                print(temp.data, end=" ")

                if temp.left:
                    arr.append(temp.left)

                if temp.right:
                    arr.append(temp.right)

            level += 1

        print("\nHeight:", level - 1)


# MAIN PROGRAM
b1 = BST()

# INSERT VALUES
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(300))
b1.insert(Node(50))
b1.insert(Node(500))
b1.insert(Node(70))
b1.insert(Node(20))
b1.insert(Node(12))
# TRAVERSALS
print("\nInorder:")
b1.inorder(b1.root)

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

# COUNT NODES
print("\nTotal nodes:", b1.count_nodes(b1.root))
print("Leaf nodes:", b1.count_leaf(b1.root))
print("Non-leaf nodes:", b1.count_nonleaf(b1.root))

# MINIMUM AND MAXIMUM
b1.findminmax()

# LEVEL ORDER
print("\nLevel Order:")
b1.level_order(b1.root)

# SEARCH
if b1.search(450):
    print("\nNode Found")
else:
    print("\nNode Not Found")

# DELETE
b1.root = b1.delete(b1.root, 4)

print("\nAfter Deletion:")
b1.inorder(b1.root)
