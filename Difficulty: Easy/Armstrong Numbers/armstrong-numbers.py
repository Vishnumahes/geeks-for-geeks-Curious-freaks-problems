#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        hundreds = n // 100  # Get the hundreds digit
        tens = (n // 10) % 10  # Get the tens digit
        ones = n % 10  # Get the ones digit

        # Calculate the sum of the cubes of the digits
        sum_of_cubes = (hundreds ** 3) + (tens ** 3) + (ones ** 3)

        # Check if the sum of the cubes equals the number itself
        if sum_of_cubes == n:
            return "true"
        else:
            return "false"
        
        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends