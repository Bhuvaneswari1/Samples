class node1:
  def __init__(self,data):
    self.value=data
    self.right=None
    self.left=None

def insert_node(root,data):
  if root is None:
    root=node1(data)
  elif root.value > data:
    if root.left is None:
      root.left=node1(data)
    else:
      insert_node(root.left,data)
  elif root.value < data:
    if root.right is None:
      root.right=node1(data)
    else:
      insert_node(root.right,data)

def LCA(root,L_val,R_val):
  if root is None:
    return None
  elif L_val > root.value and R_val > root.value:
    return(LCA(root.right,L_val,R_val))
  elif L_val < root.value and R_val < root.value:
    return (LCA(root.left,L_val,R_val))
  else:
    return root.value

n=int(input())
val=list(map(eval,input().split()))
u,v=map(eval,input().split())
R=node1(val[0])
for i in range(1,n):
  insert_node(R,val[i])
print(LCA(R,u,v))
