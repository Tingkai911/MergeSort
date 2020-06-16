var arr = [20, 60, 30, 70, 40, 50, 10, 5, 0];
console.log(arr);
mergeSort(arr);
console.log(arr);

function mergeSort(arr) {
    if (arr.length == 1) {
        return;
    }

    const MIDDLE = Math.floor(arr.length / 2);
    // create temp left and right arrays
    var left_array = [];
    var right_array = [];
    const LEFT_ARRAY_SIZE = MIDDLE;
    const RIGHT_ARRAY_SIZE = arr.length - MIDDLE;
    for (let i = 0; i < LEFT_ARRAY_SIZE; i++) {
        left_array.push(arr[i]);
    }
    for (let i = 0; i < RIGHT_ARRAY_SIZE; i++) {
        right_array.push(arr[MIDDLE + i]);
    }
    // console.log(MIDDLE);
    // console.log(LEFT_ARRAY_SIZE);
    // console.log(RIGHT_ARRAY_SIZE);
    // console.log(left_array);
    // console.log(right_array);
    mergeSort(left_array);
    mergeSort(right_array);
    merge(arr, left_array, right_array);
} 

function merge(arr, left_array, right_array) {
    var i = j = k = 0;

    while (i < left_array.length && j < right_array.length) {
        if(left_array[i] <= right_array[j]) {
            arr[k] = left_array[i];
            i++;
        } else {
            arr[k] = right_array[j];
            j++;
        }
        k++;
    }

    // copy the left over elements to the end of array if any
    while (i < left_array.length) {
        arr[k] = left_array[i];
        i++;
        k++;
    }

    while (j < right_array.length) {
        arr[k] = right_array[j];
        j++;
        k++;
    }
}
