# Function to print the required pattern
def printPattern(n):
     
    # arr[][] will store the pattern matrix
    arr = [[0 for i in range(n)]
              for j in range(n)]
    p = 1
 
    # Store the values for upper
    # triangle of the pattern
    for k in range(n):
        i = k
        j = 0
        while (i >= 0):
            arr[i][j] = p
            p += 1
            i = i - 1
            j = j + 1
     
    # Store the values for lower triangle
    # of the pattern
    for k in range(1, n, 1):
        j = k
        i = n - 1
        f = k
        while (i >= f):
            arr[i][j] = p
            p += 1
            i = i - 1
            j = j + 1
     
    # Print the pattern
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            print(arr[i][j], end = " ")
         
        print("\n", end = "")
 
# Driver code
if __name__ == '__main__':
    n = 4
 
    printPattern(n)





