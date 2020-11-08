输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        
        # 根节点
        root = TreeNode(preorder[0])
        # 获取根节点在 inorder 中的索引
        idx = inorder.index(preorder[0])
        # 左子树
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        # 右子树
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root

