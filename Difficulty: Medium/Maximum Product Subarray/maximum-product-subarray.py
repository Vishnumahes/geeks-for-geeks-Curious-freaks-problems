#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		n=len(arr)
		res=float('-inf')
		prefixsum=1
		suffixsum=1
		for i in range(len(arr)):
		    if prefixsum==0:
		        prefixsum=1
		    if suffixsum==0:
		        suffixsum=1
            prefixsum=prefixsum*arr[i]
            suffixsum=suffixsum*arr[n-i-1]
            res=max(res,prefixsum,suffixsum)
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