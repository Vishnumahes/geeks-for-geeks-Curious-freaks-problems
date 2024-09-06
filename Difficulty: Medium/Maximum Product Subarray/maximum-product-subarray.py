class Solution:

    # Function to find maximum product subarray
    def maxProduct(self, arr, n):
        # Initial values
        res = float('-inf')  # To handle negative numbers
        prefixsum = 1
        suffixsum = 1
        
        for i in range(n):
            # Reset prefix and suffix if they become 0
            if prefixsum == 0:
                prefixsum = 1
            if suffixsum == 0:
                suffixsum = 1
            
            # Calculating prefix and suffix product
            prefixsum *= arr[i]
            suffixsum *= arr[n - i - 1]
            
            # Update result with the maximum of the current prefix and suffix products
            res = max(res, prefixsum, suffixsum)
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends