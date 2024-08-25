class Solution:
    def hasArrayTwoCandidates(self, arr, x):
        arr.sort()  # O(n log n)
        l = 0
        r = len(arr) - 1
        
        while l < r:
            current_sum = arr[l] + arr[r]
            if current_sum == x:
                return True
            elif current_sum < x:
                l += 1
            else:
                r -= 1
        
        return False


		  


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        #print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends