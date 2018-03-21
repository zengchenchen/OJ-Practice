# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root


class Solution(object):
    def buildTree1(self, preorder, inorder):
        if preorder == []:
            return []
        if len(inorder) == 1:
            root = TreeNode(inorder[0])
            return root
        else:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            if ind == 0:
                root.left = None
                root.right = self.buildTree(preorder[:], inorder[ind + 1:])
                return root
            elif ind == len(inorder) - 1:
                root.left = self.buildTree(preorder[:], inorder[0:ind])
                root.right = None
                return root
            else:
                root.left = self.buildTree(preorder[0:ind], inorder[0:ind])
                root.right = self.buildTree(preorder[ind:], inorder[ind + 1:])
                return root


a = Solution()
print(a.buildTree([],
                  []))
