class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.height = 0

    def pre_order_traversal(self, node, result):
        if node:
            result.append(node.val)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    def post_order_traversal(self, node, result):
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.val)
        return result

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)
        return result

    def tree_insert(self, val):
        new_node = TreeNode(val)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current:
            if val < current.val:
                if not current.left:
                    current.left = new_node
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    break
                current = current.right

    def tree_search(self, node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return self.tree_search(node.left, val)
        return self.tree_search(node.right, val)

    def maximum(self, node):
        while node.right:
            node = node.right
        return node

    def minimum(self, node):
        while node.left:
            node = node.left
        return node

    def tree_successor(self, node):
        if node.right:
            return self.minimum(node.right)
        current = self.root
        successor = None
        while current:
            if node.val < current.val:
                successor = current
                current = current.left
            elif node.val > current.val:
                current = current.right
            else:
                break
        return successor

    def tree_predecessor(self, node):
        if node.left:
            return self.maximum(node.left)
        current = self.root
        predecessor = None
        while current:
            if node.val > current.val:
                predecessor = current
                current = current.right
            elif node.val < current.val:
                current = current.left
            else:
                break
        return predecessor

    def common_ancestor(self, root, p, q):
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            return self.common_ancestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.common_ancestor(root.right, p, q)
        return root

    def balance_bst(self):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def build_balanced_bst(sorted_vals):
            if not sorted_vals:
                return None
            mid = len(sorted_vals) // 2
            node = TreeNode(sorted_vals[mid])
            node.left = build_balanced_bst(sorted_vals[:mid])
            node.right = build_balanced_bst(sorted_vals[mid + 1:])
            return node

        sorted_vals = inorder(self.root)
        self.root = build_balanced_bst(sorted_vals)

bst = BinarySearchTree()
values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
    bst.tree_insert(val)

print("Inorder Traversal:", bst.inorder_traversal(bst.root, []))
print("Preorder Traversal:", bst.pre_order_traversal(bst.root, []))
print("Postorder Traversal:", bst.post_order_traversal(bst.root, []))
print("Minimum:", bst.minimum(bst.root).val)
print("Maximum:", bst.maximum(bst.root).val)
print("Search for 15:", bst.tree_search(bst.root, 15).val)
successor = bst.tree_successor(bst.tree_search(bst.root, 15))
if successor:
    print("Successor of 15:", successor.val)
predecessor = bst.tree_predecessor(bst.tree_search(bst.root, 15))
if predecessor:
    print("Predecessor of 15:", predecessor.val)
bst.balance_bst()
print("Inorder Traversal after balancing:", bst.inorder_traversal(bst.root, []))
