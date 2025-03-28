# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []

        def traverse(node, array):
            if node is None:
                return
            traverse(node.left, array)
            array.append(node.val)
            traverse(node.right, array)

        traverse(root, array)
        return array




