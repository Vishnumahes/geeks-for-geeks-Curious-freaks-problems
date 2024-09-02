#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        res=0
        maxi=arr[0]
        start=0
        ansStart=0
        ansEnd=0
        for i in range(len(arr)):
            res+=arr[i]
            if res>maxi:
                maxi=res
                ansStart=start
                ansEnd=i
            
            if(res<0):
                res=0
                start=i+1
        return maxi
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends