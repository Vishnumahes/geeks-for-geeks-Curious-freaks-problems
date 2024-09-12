#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, N): 
        # code here
        for i in range(N):
            for j in range(i, N):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        
        # Step 2: Reverse each column to rotate by 90 degrees anticlockwise
        for i in range(N):
            for j in range(N // 2):
                a[j][i], a[N - 1 - j][i] = a[N - 1 - j][i], a[j][i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends