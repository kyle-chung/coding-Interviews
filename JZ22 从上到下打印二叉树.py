从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]

题目要求的二叉树的 从上至下 打印（即按层打印），又称为二叉树的 广度优先搜索（BFS）
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []

        while stack:
            temp = stack.pop(0)
            res.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                    stack.append(temp.right)
        
        return res
