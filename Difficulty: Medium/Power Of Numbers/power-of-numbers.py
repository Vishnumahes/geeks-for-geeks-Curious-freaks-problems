#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        mod =(10**9)+7
        res=pow(N,R,mod)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends