import pytest
from quick_sort import quick_sort

@ pytest.mark.parametrize(
    "test_list,expected",[
    ([8,4,23,42,16,15],[4, 8, 15, 16, 23, 42]),

    ([20,18,12,8,5,-2],[-2, 5, 8, 12, 18, 20] ),
    ([5,12,7,5,5,7],[5, 5, 5, 7, 7, 12]),
    ([2,3,5,7,13,11],[2, 3, 5, 7, 11, 13] )
    ])

def test_quick_sort(test_list,expected):
    result=test_list
    actual=quick_sort(result,0,len(result)-1)
    assert result==expected
