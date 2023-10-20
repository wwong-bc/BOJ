import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.left = None
        self.right = None

    def preorder(self):
        travel = []
        travel.append(self.index)
        if self.left:
            travel += self.left.preorder()
        if self.right:
            travel += self.right.preorder()
        return travel

    def postorder(self):
        travel = []
        if self.left:
            travel += self.left.postorder()
        if self.right:
            travel += self.right.postorder()
        travel.append(self.index)
        return travel
    def insert(self, node):
        if node.x < self.x:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node

class Tree:
    def __init__(self):
        self.root = None
    def insert(self, node):
        if not self.root:
            self.root = node
        else:
            self.root.insert(node)
        

    
def makeTree(nodeinfo):
    sorted_node = sorted(nodeinfo, key = lambda elem :(elem[1], -elem[0]), reverse=True)
    # print(sorted_node)
    tree = Tree()
    for node in sorted_node:
        x, y = node
        index = nodeinfo.index(node) + 1
        new_node = Node(x, y, index)
        tree.insert(new_node)
    return tree

def solution(nodeinfo):
    answer = []
    tree = makeTree(nodeinfo)
    answer = [tree.root.preorder(), tree.root.postorder()]
    return answer
