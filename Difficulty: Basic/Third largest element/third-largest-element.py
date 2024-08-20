class Solution:
    def thirdLargest(self, arr):
        maxi1,maxi2,maxi3=-1,-1,-1
        for i in arr:
            if i>maxi1:
                maxi3=maxi2
                maxi2=maxi1
                maxi1=i
            elif i>maxi2:
                maxi3=maxi2
                maxi2=i
            elif i>maxi3:
                maxi3=i 
        return maxi3 
        
        




            


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))

# } Driver Code Ends