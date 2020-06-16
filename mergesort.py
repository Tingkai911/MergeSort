import math

def main():
    arr = [20, 60, 30, 70, 40, 50, 10]
    print(arr)
    # left_index = 0
    # right_index = len(arr) - 1
    # mergeSort(arr, left_index, right_index)
    mergeSort(arr)
    print(arr)

# def mergeSort (arr, left_index, right_index):
#     #base case
#     if left_index == right_index:
#         return
    
#     middle_index = int(math.floor((left_index + right_index) / 2))
    
#     #recursive case
#     mergeSort(arr, left_index, middle_index)
#     mergeSort(arr, middle_index + 1, right_index)

#     #create temporary arrays for left and right half
#     left_half_size = middle_index - left_index + 1
#     temp_left_array = []
#     for i in range(left_half_size):
#         temp_left_array.append(arr[left_index + i])
#     right_half_size = right_index - middle_index
#     temp_right_array = []
#     for i in range(right_half_size):
#         temp_right_array.append(arr[middle_index + 1 + i])

#     #comparing and sorting
#     i = j = 0
#     k = left_index

#     while i < left_half_size and j < right_half_size:
#         if temp_left_array[i] <= temp_right_array[j]:
#             arr[k] = temp_left_array[i]
#             i += 1
#         else:
#             arr[k] = temp_right_array[j]
#             j += 1
#         k += 1

#     #copy the remaining elements to the end of array if any
#     while i < left_half_size:
#         arr[k] = temp_left_array[i]
#         i += 1
#         k += 1
#     while j < right_half_size:
#         arr[k] = temp_right_array[j]
#         j += 1
#         k += 1
    

def mergeSort(arr):
    #base case
    if len(arr) == 1:
        return
    
    #create temporary arrays for left and right half
    middle_index = int(math.floor(len(arr) / 2))
    left_half_array = arr[:middle_index]
    right_half_array = arr[middle_index:]
    mergeSort(left_half_array)
    mergeSort(right_half_array)

    #comparing and sorting
    i = j = k = 0
    while i < len(left_half_array) and j < len(right_half_array):
        if left_half_array[i] <= right_half_array[j]:
            arr[k] = left_half_array[i]
            i += 1
        else:
            arr[k] = right_half_array[j]
            j += 1
        k += 1

    #copy the remaining elements to end of array if any
    while i < len(left_half_array):
        arr[k] = left_half_array[i]
        i += 1
        k += 1
    while j < len(right_half_array):
        arr[k] = right_half_array[j]
        j += 1
        k += 1


if __name__ =="__main__":
    main()