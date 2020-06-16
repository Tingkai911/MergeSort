def main():
    arr = [
        [1,2,3,4,5],
        [10,12,15],
        [6,7,8,9],
        [11,13,14,16],
        [32, 35, 70]
    ]

    temp = []
    for i in range(len(arr)):
        temp.extend(arr[i])
    # temp = [20, 60, 30, 70, 40, 50, 10]
    print(temp)
    print(mergeSort(temp))
    print(temp)


def mergeSort(arr):
    if len(arr) == 1:
        return
    middle = len(arr) // 2
    L = arr[:middle]
    R = arr[middle:]
    mergeSort(L)
    mergeSort(R)
    merge(arr, L, R)
    # return arr


def merge(arr, left_half_array, right_half_array):
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
    # return arr


if __name__ == "__main__":
    main()