class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTreeNode(arr):
    nodes = [TreeNode(val) if val else None for val in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def printTreeNode(root):
    queue = [root]
    arr = []
    todo = 1 if root else 0
    while todo > 0:
        node = queue.pop(0)
        if node:
            todo -= 1
            arr += node.val,
            for kid in node.left, node.right:
                queue += kid,
                if kid:
                    todo += 1
        else:
            arr += None,
    print(arr)
    return arr
