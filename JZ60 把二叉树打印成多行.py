剑指 Offer 32 - II. 从上到下打印二叉树 II

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
        # 思路：层序遍历二叉树分开保存每一层的节点值，初始化res：输出保存列表；nodel_list是保存节点列表，列表内容更新来自于每一层
        #       layer_nodel列表；layer_val 保存每一层值；
        if not root:
            return []
        res = []
        node_list = []
        node_list.append(root)

        while node_list:
            layer_val = []
            layer_node = []
            while node_list:
                node = node_list.pop(0)
                layer_val.append(node.val)

                if node.left: layer_node.append(node.left)
                if node.right: layer_node.append(node.right)
            node_list.extend(layer_node)
            res.append(layer_val)
        return res



recur:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(node, level):
            if not node:return
            # 这句是关键
            # 当发现节点为第level层，而res有len（res）层，即只有第len（res）-1 = level-1层，res增加一个list
            # 例如节点level == 1，而len（res） == 1，即只有第0层
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        return res
    






