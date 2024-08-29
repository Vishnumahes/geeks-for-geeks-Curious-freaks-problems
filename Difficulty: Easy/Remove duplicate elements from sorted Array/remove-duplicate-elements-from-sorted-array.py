class Solution:
    def remove_duplicate(self, arr):
        n = len(arr)
        
        if n == 0 or n == 1:
            return n

        # Index to place the next unique element
        j = 0
        
        for i in range(0, n-1):
            # If the current element is not equal to the next element
            if arr[i] != arr[i+1]:
                arr[j] = arr[i]
                j += 1
        
        # Store the last element
        arr[j] = arr[n-1]
        j += 1
        
        return j


# Driver Code Ends

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.remove_duplicate(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()

# } Driver Code Ends