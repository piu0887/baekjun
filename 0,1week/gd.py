import sys
input = sys.stdin.readline

N_node =int(input())
inputs=[]
for _ in range(N_node):
    inputs.append(input().split())

class Node():
    def __init__(self, name,left,right) -> None:
        self.name = name
        self.left = left
        self.right = right
    
def preorder(root):
    print(root.name, end ='')
    if root.left !='.':
        preorder(tree[root.left])
    if root.right !='.':
        preorder(tree[root.right])

def inorder(root):
    if root.left !='.':
        inorder(tree[root.left])
    print(root.name, end='')
    if root.right !='.':
        inorder(tree[root.right])

def postorder(root):
    if root.left !='.':
        postorder(tree[root.left])
    if root.right !='.':
        postorder(tree[root.right])
    print(root.name, end='')


tree = {}

for root, left, right in inputs:
    tree[root] = Node(root,left,right)

preorder(tree['A'])            
print()
inorder(tree['A'])
print()
postorder(tree['A'])


    