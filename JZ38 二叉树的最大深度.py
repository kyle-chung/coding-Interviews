给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

自创：双stack
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack1 = [root]
        stack2 = []
        depth = 0

        while stack1 or stack2:
            if stack1: depth += 1
            while stack1:
                temp = stack1.pop()
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)

            if stack2: depth += 1
            while stack2:
                temp = stack2.pop()
                if temp.left:
                    stack1.append(temp.left)
                if temp.right:
                    stack1.append(temp.right)

        return depth
    
    recur：
    class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        left_high = self.maxDepth(root.left)
        right_high = self.maxDepth(root.right)

        return max(left_high,right_high) + 1


