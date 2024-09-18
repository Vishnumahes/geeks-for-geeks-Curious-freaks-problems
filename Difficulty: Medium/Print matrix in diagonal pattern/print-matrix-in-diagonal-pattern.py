# Your task is to complete this function
class Solution:
    def matrixDiagonally(self, mat):
        if not mat or not mat[0]:
            return []

        n = len(mat)
        m = len(mat[0])
        result = []

        # There are n + m - 1 diagonals in total for an n x m matrix.
        for diag in range(n + m - 1):
            # Depending on the diagonal index, decide whether to traverse upwards or downwards
            if diag % 2 == 0:
                # Upward diagonal traversal
                i = min(diag, n - 1)
                j = diag - i
                while i >= 0 and j < m:
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
            else:
                # Downward diagonal traversal
                j = min(diag, m - 1)
                i = diag - j
                while i < n and j >= 0:
                    result.append(mat[i][j])
                    i += 1
                    j -= 1

        return result

        # code here


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends