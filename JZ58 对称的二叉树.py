请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false

recur：
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True
 
自创：双栈
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [root]
        l = []
        temp_l = []
        while stack or l:
            while stack:
                temp = stack.pop(0)
                if temp != 'x':
                    if temp.left:
                        l.append(temp.left)
                    else: l.append('x')
                    if temp.right:
                        l.append(temp.right)
                    else: l.append('x')

            for i in range(len(l)):
                if l[i] == 'x':
                    temp_l.append(l[i])
                else:
                    temp_l.append(l[i].val)
            if temp_l != temp_l[::-1]: return False
            temp_l = []


            while l:
                temp = l.pop(0)
                if temp != 'x':
                    if temp.left:
                        stack.append(temp.left)
                    else: stack.append('x')
                    if temp.right:
                        stack.append(temp.right)
                    else: stack.append('x')
            for i in range(len(stack)):
                if stack[i] == 'x':
                    temp_l.append('x')
                else:
                    temp_l.append(stack[i].val)
            if temp_l != temp_l[::-1]: return False
            temp_l = []
        
        return True
