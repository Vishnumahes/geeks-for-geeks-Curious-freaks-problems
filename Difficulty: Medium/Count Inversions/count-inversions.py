class Solution:
    # Function to merge two halves and count inversions
    def merge(self, arr, temp_arr, left, mid, right):
        i = left    # Pointer for the left subarray
        j = mid + 1 # Pointer for the right subarray
        k = left    # Pointer for the temporary array
        inv_count = 0
        
        # Use two pointers to merge arrays and count inversions
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        
        # Copy remaining elements from the left subarray
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        
        # Copy remaining elements from the right subarray
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        
        # Copy sorted subarray into the original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]
            
        return inv_count
    
    # Function to divide the array into halves and count inversions
    def merge_sort_and_count(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
    
            inv_count += self.merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += self.merge_sort_and_count(arr, temp_arr, mid + 1, right)
    
            inv_count += self.merge(arr, temp_arr, left, mid, right)
    
        return inv_count
    
    def inversionCount(self, arr, n):
        temp_arr = [0] * n
        return self.merge_sort_and_count(arr, temp_arr, 0, n - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a, n))

# } Driver Code Ends