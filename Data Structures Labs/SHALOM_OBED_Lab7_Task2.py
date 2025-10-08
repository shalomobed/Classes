def print_subsets(arr):
    #Printing all possible subsets of a list using recursion.
    def subsetRecur(i, subset):
        #Base case
        if i == len(arr):
            print(subset)
            return
        
        #Recursive case 1
        subset.append(arr[i])
        subsetRecur(i + 1, subset)
        
        #Recursive case 2
        subset.pop()
        subsetRecur(i + 1, subset)
    
    subsetRecur(0, [])

#Driver code
if __name__ == "__main__":
    arr = [1, 2, 3]
    res = print_subsets(arr)
    