#User function Template for python3

def isSubset( a1, a2, n, m):
    dict1 = {}
    
    for i in range(n):
        if a1[i] in dict1:
            dict1[a1[i]] += 1
        else:
            dict1[a1[i]] = 1
    
  
    for i in range(m):
        if a2[i] in dict1 and dict1[a2[i]] > 0:
            dict1[a2[i]] -= 1
        else:
            return "No"
    
    return "Yes"
        
        
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends