'''
Given Array is sorted:
1. Single element present in the array
2. Array is empty, constraints say the array will never be empty

Edge Cases if array is not sorted:
1. Array is in ascending/descending order
--> Use two-pointer approach, start pointer starts from beginning and end from the end of the array. 
    Ensure start < end and end - start + 1 > k, break when end-start+1 == k
2. The array is not sorted then, sort the array and perform step 1.

Approaches:
Brute Force:
Time: O(nlogn + klogk)
Space: O(1)
Sort the array based on difference of all the elements and given number, x.
Then, sort the first k elements and return that as result.

2nd Approach: Use heap
Time: O(nlogk + klogk)
Space: O(k) for heap
Maintain a max heap of size k, and keep inserting the elements based on their difference with given number, x when the size goes beyond k simple pop the max difference element.

3rd Approach: Use the information (Sorted array)
Time: O(logn + k)
Space: O(1)
Step1. Use binary search to find the index of the element if it's present else it's nearest left index
Step2. declare left = index from above binary search - 1 and right = binary search index
Step3. Run loop k times, keep comparing difference of left and right element with given number, x and slide left or right based on the difference. If left's diff is less or equal to the diff on right, decrement left until left reaches 0 else increment right until right reaches len(array)-1, which are the edge cases to be handled.

Optimised Approach:
Time: O(log(n-k) + k)
Space: O(1)
Similar to the above approach with a catch that we are given a number and have to find closest k elements to it, deducing it to conclusion, we can construct the question as find k closest numbers from given number(k//2 from left, k//2 from right or in similar fashion). Now, think of the upper bound to left --> it will be len(arr)-k.
So, left = 0, right = len(arr) - k
'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k
        # perform binary search
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left : left + k]          
            
        
        
        
        
        """
        # get leftmost index for the given number, x
        index = bisect.bisect_left(arr, x)
        left = index - 1 if index > 0 else 0
        right = index
        
        while right-left+1 < k:
            if left == 0:
                right += 1
                continue
            if right == len(arr):
                left -= 1
                continue
            
            if (x - arr[left]) <= (arr[right] - x):
                left -= 1
            else:
                right += 1
        
        return arr[left:right+1]
        """
        
        
        
        
        
        