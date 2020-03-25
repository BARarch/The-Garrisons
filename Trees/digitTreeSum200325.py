#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def digitTreeSum(t):
    def digitTreeSumHelp(t, val):
        left = 0
        right = 0
        if t.left:
            left = digitTreeSumHelp(t.left, val + str(t.value))
        if t.right:
            right = digitTreeSumHelp(t.right, val + str(t.value))

        if left == 0 and right == 0:
            return int(val + str(t.value))
        else:
            return left + right

    return digitTreeSumHelp(t, '')

