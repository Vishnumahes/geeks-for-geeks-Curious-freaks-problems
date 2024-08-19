#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        
        minimum = arr[0]
        maximum = arr[0]
    
    # Loop through the array to find the minimum and maximum
        for num in arr[1:]:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
    
    # Return the minimum and maximum values
        return minimum, maximum
                
                
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1


# } Driver Code Ends