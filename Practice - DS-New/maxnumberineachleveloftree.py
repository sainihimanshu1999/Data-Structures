#User function Template for python3
def fun(res,root,d):
        if root is None:
            return None
        if(d==len(res)):
            res.append(root.data)
        else:
            res[d] = max(res[d],root.data)
        
        fun(res,root.left,d+1)
        fun(res,root.right,d+1)


class Solution:
    
    def largestValues(self, root):
        a = []
        fun(a,root,0)
        return a