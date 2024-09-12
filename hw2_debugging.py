'''
This module implements the merge sort alogorithm using helper functions
'''
import logging
import rand

logging.basicConfig(filename='debugging.log',encoding='utf-8',level=logging.DEBUG, 
                                     format='%(asctime)s %(levelname)s %(message)s')
logging.debug("NEW LOG hw2_debugging file:")

def merge_sort(input_arr):
    '''
    Performing merge_sort on input_arr
    '''
    logger= logging.getLogger(__name__)
    logger.debug("merge_sort called with: %r", input_arr)
    if len(input_arr) == 1:
        logger.debug("Single element array returning: %r", input_arr)
        return input_arr

    half = len(input_arr) // 2
    logger.debug("half:%r",half)
    left_sorted = merge_sort(input_arr[:half])
    right_sorted = merge_sort(input_arr[half:])
    result = re_combine(left_sorted,right_sorted)
    # result = re_combine(merge_sort(arr[:half]), merge_sort(arr[half:]))
    logger.debug("result after combine: %r",result)
    return result
def re_combine(left_arr, right_arr):
    '''
    this function re_combine two sorted array into one sorted array
    '''
    logger= logging.getLogger(__name__)
    logger.debug("Recombining %r and %r",left_arr,right_arr)
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1
    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index +=1
    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index +=1
    logger.debug("Merged array: %r",merge_arr)
    return merge_arr
arr = rand.random_array([None] * 20)

logging.debug("Initial random array: %r",arr)

arr_out = merge_sort(arr)
logging.debug("array output: %r",arr_out)


print(arr_out)
