# Merge Sort

## promblem Domain:

Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.

## Pseudocode

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```
## Algorithm

1. Creat a function take list of integers

2. declare n length of array

3. declare mid half of n

4. Sorting the left half

5. Sorting the right half

6. Creat function called merge take 3 arguments((left,right,arr))

7. call merge for (left,right,arr)

8. declare i,j,k with 0

9. while loop Copy data to temp arrays left[] and right[]

10. Checking if any element was left
## Trace

Sample Array: [8,4,23,42,16,15]


left 	    |  right 	        |new list
------------|-------------------|-----------------------
[4] 	    |  [23] 	        |[4, 23]
[8] 	    |  [4, 23] 	        |[4, 8, 23]
[16] 	    |  [15] 	        |[15, 16]
[42] 	    |  [15, 16] 	    |[15, 16, 42]
[4, 8, 23] 	|  [15, 16, 42] 	|[4, 8, 15, 16, 23, 42]

## Code

```
def merge_sort(arr):
  n = len(arr)
  if n>1 :
    mid = n//2
    left =arr[0:mid]
    merge_sort(left)
    right = arr[mid:n]
    merge_sort(right)
    merge(left,right,arr)
    return arr
def merge(left,right,arr):
  i,j,k = 0,0,0
  while i<len(left) and j<len(right):
    if left[i] <= right[j]:
      arr[k]=left[i]
      i += 1
    else:
      arr[k]=right[j]
      j += 1
    k += 1
  if len(left)==i:
     for item in right[j:]:
                arr[k] = item
                k += 1
  else:
            for item in left[i:]:
                arr[k] = item
                k += 1
number_list = [20,18,12,8,5,-2]
merge_sort(number_list)
print(number_list)
```

## Tests

```
import pytest
from merge_sort import merge_sort

@ pytest.mark.parametrize(
    "test_list,expected",[
    ([8,4,23,42,16,15],[4, 8, 15, 16, 23, 42]),

    ([20,18,12,8,5,-2],[-2, 5, 8, 12, 18, 20] ),
    ([5,12,7,5,5,7],[5, 5, 5, 7, 7, 12]),
    ([2,3,5,7,13,11],[2, 3, 5, 7, 11, 13] )
    ])

def test_insertion_sort(test_list,expected):
    actual=merge_sort(test_list)
    assert actual==expected
```

## Big O

Time: O(n*log_n)
Space:O(n)
