从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

自创：双栈

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = [root]
        l = []
        res = [[root.val]]

        while stack or l:
            while stack:
                temp = stack.pop(0)
                if temp.left:
                    l.append(temp.left)
                if temp.right:
                    l.append(temp.right)
            temp = []
            for i in l:
                temp += [i.val]
            if temp: res.append(temp)

            while l:
                temp = l.pop(0)
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
            temp = []
            for i in stack:
                temp += [i.val]
            if temp: res.append(temp)
        
        return res
