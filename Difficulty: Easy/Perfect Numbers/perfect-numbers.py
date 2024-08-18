#User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        if N <= 1:
            return 0

        sum_of_divisors = 1  # 1 is always a divisor

        i = 2
        while i * i <= N:
            if N % i == 0:  # If i is a divisor
                sum_of_divisors += i
                if i != N // i:  # To avoid adding the square root twice
                    sum_of_divisors += N // i
            i += 1

        return 1 if sum_of_divisors == N else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends