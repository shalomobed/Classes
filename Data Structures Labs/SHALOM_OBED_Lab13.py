def counting_sort(input_arr, minimum, maximum):
    """
    Implement the counting sort algorithm in Python, assuming the range of input numbers 
    is [MIN,MAX]. Consider optimizing the extra space usage by using the range of the input. 
    """
    #The range would be from maximum to minimum + 1
    count = [0] * (maximum - minimum + 1)
    #The output array would be the length of the input array
    output = [0] * len(input_arr)

    #Add the count for all the numbers in the array - minimum
    for i in range(len(input_arr)):
        key = input_arr[i] - minimum
        #The count for (number -  minimum) is added to the count array
        count[key] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(input_arr) - 1, -1, -1):
        key = input_arr[i] - minimum
        count[key] -= 1
        output[count[key]] = input_arr[i]
    return output
#Sample input 1
arr1 = [527, 8763, 12, 45, 9076, 298, 7603, 432, 1, 30456]
sorted_arr = counting_sort(arr1, min(arr1), max(arr1))
print(sorted_arr)

#Sample input 2
arr2 = [10, 5, 7, 12, 8, 5, 14, 15, 6, 13]
sorted_arr = counting_sort(arr2, min(arr2), max(arr2))
print(sorted_arr)

#Sample input 3
arr3 = [2300, 2298, 2299, 2302, 2307, 2305, 2304, 2302, 2306, 2303]
sorted_arr = counting_sort(arr3, min(arr3), max(arr3))
print(sorted_arr)


