# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node,maxdepth,count):
            if node == None:
                if count > maxdepth:
                    maxdepth = count
                    return maxdepth
            count +=1
            rightnode=traverse(node.right,maxdepth,count)
            leftnode=traverse(node.left,maxdepth,count)
            if rightnode > leftnode:
                return rightnode
            else:
                return leftnode
        
        return traverse(root,0,0)
        
    
