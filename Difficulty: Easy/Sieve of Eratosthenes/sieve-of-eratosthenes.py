class Solution:
    def sieveOfEratosthenes(self, n):
        # Initialize a list to mark prime numbers
        prime = [True for i in range(n+1)]
        p = 2
        
        # Start Sieve of Eratosthenes algorithm
        while (p * p <= n):
            if prime[p]:
                # Mark all multiples of p as False (not prime)
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        
        # Collect and return the prime numbers
        prime_numbers = []
        for p in range(2, n+1):
            if prime[p]:
                prime_numbers.append(p)
        
        return prime_numbers

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends