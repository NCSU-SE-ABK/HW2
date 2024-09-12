'''Test cases for mergesort'''
from hw2_debugging import merge_sort

def test_p():
    '''Consider positive numbers'''
    a = [9,4,5,2,1,10,3]
    expected = [1,2,3,4,5,9,10]
    assert merge_sort(a) == expected

def test_n():
    '''Consider negative numbers'''
    a = [-22,-9,-15,-8,-2,0]
    expected = [-22,-15,-9,-8,-2,0]
    assert merge_sort(a) == expected

def test_d():
    '''Consider duplicates'''
    a = [2,3,5,5,5,3,3,2]
    expected = [2,2,3,3,3,5,5,5]
    assert merge_sort(a) == expected
