
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        rem=1
        if a>b:
            Dividend=a
            Divisor=b
        else:
            Dividend=b
            Divisor=a
        while rem!=0:
            rem=Dividend%Divisor
            if rem!=0:
                Dividend=Divisor
                Divisor=rem
        return Divisor
            
        
        
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

# } Driver Code Ends