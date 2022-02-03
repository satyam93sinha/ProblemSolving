"""
Deduction:
There are four arrays namely, nums1, nums2, nums3 and nums4 and we have to find the total number of tuples such that:
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

As the sum has to be zero, we can deduce that these arrays can contain negative integers too. Anyways, that is given in the question under constraints.

Edge Cases:
1. All the arrays are empty; impossible, it is a constraint
2. There is no tuple from array that can sum up to zero; return 0
3. Array elements can form single/multiple tuples whose sum is zero; 
return count
4. Arrays contain zero as its only element; return 1

Approaches:
1. Brute Force
Time: O(n**4)
Space: O(1)
Intuition:
Take four for loops and iterate over every element combination of each array and maintain a count of those sum that come up to zero.

2. Use Three & Two Sum; Convert it to single array and find 4sum; 
Won't work because if we keep elements of all the arrays into one, there is a possibility of getting zero from elements of single array and leading to wrong solution.
Time: O(n**3)
Space: O(4*n)
Intuition:
Create a nums array containing all the elements of the four arrays and sort them. Now, fix first two elements and find remaining target using Two Sum, if found increment count.

3. Use Hashing/dictionary
Time: O(n**3)
Space: O(n)
Intuition:
Convert one of the arrays to dictionary storing numbers and their frequecies in that array in order to maintain count considering duplicate entries/numbers in the array. Then, search for (num1 + num2 + num3) * -1 in this dictionary, this will ensure the sum is zero.

4. Use Addition
Time: O(n**2)
Space: O(2*n)
Intuition:
Generate all the combinations of nums1 and nums2 elements added and store them in a hashmap/dictionary with their sum frequencies(because one sum could appear multiple times) and then, find those elements in combinations of nums3 and nums4 added/summed combinations.
"""

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Time: O(n**2)
        # Space: O(2*n) ~ O(n)
        # generate a dictionary containing sum of all the elements from nums3 and nums4 or (any two arrays)
        nums_3_4_dict = collections.defaultdict(int)
        for num3 in nums3:
            for num4 in nums4:
                nums_3_4_dict[num3 + num4] += 1
        # check if the sum is equal to target or zero for this question
        # num1 + num2 + num3 + num4 == 0 implies
        # num1 + num2 == -(num3 + num4)
        count = 0
        for num1 in nums1:
            for num2 in nums2:
                if (num1 + num2) * -1 in nums_3_4_dict:
                    count += nums_3_4_dict[(num1 + num2) * -1]
        return count
        
        
        """
        # Time: O(n**3)
        # Space: O(n)
        
        nums4_dict = collections.Counter(nums4)
        count = 0
        for num1 in nums1:
            for num2 in nums2:
                for num3 in nums3:
                    if (num1 + num2 + num3)*-1 in nums4_dict:
                        count += nums4_dict[-(num1 + num2 + num3)]
        
        return count
        """