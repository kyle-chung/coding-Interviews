输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        # print(preorder[0])
        ind = inorder.index(preorder[0])
        print(ind)
        root = TreeNode(preorder[0])
        left = self.buildTree(preorder[1:ind+1], inorder[:ind] ) # ind表示左子树有多少个元素，所以这里是从1到ind+1
        right = self.buildTree(preorder[ind+1:], inorder[ind+1:]) # 这里填充的是 root这个元素
        root.left = left
        root.right = right

        return root
