'''
This module implements the merge sort alogorithm using helper functions
'''
import rand


def merge_sort(input_arr):
    '''
    Performing merge_sort on input_arr
    '''
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr) // 2

    return re_combine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def re_combine(left_arr, right_arr):
    '''
    this function re_combibne two sorted array into one sorted array
    '''
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]
    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index +=1
    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index +=1

    return merge_arr
arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
