#User function Template for python3

class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        l=0
        for i in range(len(arr)):
            if arr[i]==x:
                l=i
                return l
            i+=1
        else:
            return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input().strip())
    while T > 0:
        A = [int(x) for x in input().strip().split()]
        x = int(input().strip())
        ob = Solution()
        print(ob.search(A, x))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends