# User function Template for python3

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        #code here
        if len(arr1)!=len(arr2):
            return False
        
        dictarr1={}
        dictarr2={}
        
        for i in arr1:
            if i in dictarr1:
                dictarr1[i]+=1
            else:
                dictarr1[i]=1
        
        for j in arr2:
            if j in dictarr2:
                dictarr2[j]+=1
            else:
                dictarr2[j]=1
        
        if dictarr1 == dictarr2:
            return True
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        arr1 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        ob = Solution()
        if ob.check(arr1, arr2):
            print("true")
        else:
            print("false")

# } Driver Code Ends