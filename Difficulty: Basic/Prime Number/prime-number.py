#User function Template for python3

class Solution:
    def isPrime (self, N):
        # code here
        if N <= 1:
            return 0 
        i = 2
        while i * i <= N:
            if N % i == 0:
                return 0  
            i += 1

        return 1 
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends