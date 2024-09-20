
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        a=0
        b=1
        for i in range(n-1):
            
            c = (a + b)%1000000007
            a = b
            b = c
        return b
            
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends