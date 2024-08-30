class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Dictionary to store (cumulative sum: first index)
        cum_sum_map = {}
        maxlen = 0
        cum_sum = 0

        for i in range(n):
            cum_sum += arr[i]

            # If cum_sum equals k, update maxlen
            if cum_sum == k:
                maxlen = i + 1

            # If (cum_sum - k) is found in map, update maxlen
            if (cum_sum - k) in cum_sum_map:
                maxlen = max(maxlen, i - cum_sum_map[cum_sum - k])

            # Store the first occurrence of the cumulative sum
            if cum_sum not in cum_sum_map:
                cum_sum_map[cum_sum] = i

        return maxlen





#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends