# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum = []
        def subtree( node ):
            
            if node.left == None:
                left = node.val
            else:
                a, b, c = subtree( node.left )
                left = max( a, b, 0 ) + node.val
            if node.right == None:
                right = node.val
            else:
                a, b, c = subtree( node.right )
                right = max(a, b, 0) + node.val

            mid = left + right - node.val     
            max_sum.append( max( left, right, mid ) )
          
            return ( left, right, mid )

        left_gain, right_gain, mod_gain = subtree(root)
        return max(max_sum)
