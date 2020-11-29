请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。 

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
  [20,9],
  [15,7]
]

双栈：
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        node = [root]
        count = 1

        while node:
            list_val = []
            list_node = []
            while node:
                temp = node.pop(0)
                list_val.append(temp.val)
                if temp.left: list_node.append(temp.left)
                if temp.right: list_node.append(temp.right)
            node = list_node
            if count % 2 ==1: 
                res.append(list_val)
            else: res.append(list_val[::-1])
            count += 1
        return res
