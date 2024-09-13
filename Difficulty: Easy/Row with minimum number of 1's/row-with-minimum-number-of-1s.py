#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        mincount= m+1
        ind=1
        
        for i in range(1,n+1):
            cntrow= sum(a[i-1])
            
            if cntrow <mincount:
                mincount = cntrow
                ind =i
                
        return ind
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends