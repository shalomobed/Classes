#Finding the next greater for each element in an array
def nextLargerElement(arr):
    n = len(arr)
    res = [-1] * n
    stk = []

    #Traverses the array from right to left
    for i in range(n - 1, -1, -1):

        #Pops all elements that are less than or equal to the current element
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        if stk:
            res[i] = arr[stk[-1]]

        stk.append(i)
    
    return res

#Driver Code
if __name__ == "__main__":
    arr = [2, 1, 4, 3]
    res = nextLargerElement(arr)
    print(" ".join(map(str, res)))