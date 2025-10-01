def find_unique_brute_force(arr):
    #Time Complexity: O(n^2), Space Complexity: O(1)
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            return arr[i]

def find_unique_ON_ON(arr2):
    #Using a dictionary
    count_dict = {}
    for i in range(len(arr2)):
        current_number = arr2[i]

        if current_number in count_dict:
            count_dict[current_number] = count_dict[current_number] + 1
        else:
            count_dict[current_number] = 1

    for number, count in count_dict.items():
        if count == 1:
            return number
        
    return None


def find_unique_ON_O1(arr3):
    #XOR method
    result = 0
    for x in arr3:
        result ^= x
    return result
    


        
                
                     
print("Finding the unique number using a brute force approach")
print("unique number : ",find_unique_brute_force([0,2,-4,5,2,0,-4]))
print("unique number : ",find_unique_brute_force([3,3,3,3,6,6,7]))
print("unique number : ",find_unique_brute_force([1,1,1,1,1,1,1,1,2]))
print("unique number : ",find_unique_brute_force([1,0,1,2,4,2,4]))
print("unique number : ",find_unique_brute_force([3]))

print("\nFinding the unique number for O(n) time and O(n) space")
print("unique number : ",find_unique_ON_ON([0,2,-4,5,2,0,-4]))
print("unique number : ",find_unique_ON_ON([3,3,3,3,6,6,7]))
print("unique number : ",find_unique_ON_ON([1,1,1,1,1,1,1,1,2]))
print("unique number : ",find_unique_ON_ON([1,0,1,2,4,2,4]))
print("unique number : ",find_unique_ON_ON([3]))

print("\nFinding the unique number for O(n) and using no more than O(1) additional memory.")
print("unique number : ",find_unique_ON_O1([0,2,-4,5,2,0,-4]))
print("unique number : ",find_unique_ON_O1([3,3,3,3,6,6,7]))
print("unique number : ",find_unique_ON_O1([1,1,1,1,1,1,1,1,2]))
print("unique number : ",find_unique_ON_O1([1,0,1,2,4,2,4]))
print("unique number : ",find_unique_ON_O1([3]))
