# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.rob_sub(root)
        return max(res)

    def rob_sub(self, root):
        if root is None:
            return [0, 0]

        left = self.rob_sub(root.left)
        right = self.rob_sub(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res


r = TreeNode(3)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.right.left = TreeNode(3)
r.right.right = TreeNode(1)

s = Solution()
print(s.rob(r))
