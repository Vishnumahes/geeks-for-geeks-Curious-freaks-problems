# User function Template for python3
class Solution:
	def countTriplet(self, arr, n):
		# code here
		arr.sort()
		count=0
		i=len(arr)-1
		for i in range(n-1,1,-1):
		    low=0
		    high=i-1
		    while low < high:
		        sum =arr[low] +arr[high]
		        if sum == arr[i]:
		            count+=1
		            low+=1
		            high-=1
		        elif sum <arr[i]:
		            low+=1
		        elif sum >arr[i]:
		            high-=1
	    return count
		    
		    
		    
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = [int(x) for x in input().split()]

		ob = Solution()
		ans = ob.countTriplet(arr, n)
		print(ans)

# } Driver Code Ends