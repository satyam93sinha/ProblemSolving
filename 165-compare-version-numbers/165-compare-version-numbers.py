"""
Edge Cases:
1. 0-th index of version1 > version2 or vice-versa; return appropriate response
2. 0-th index are same --> check the 1st index and compare them
3. last index determines the result
4. length of version1 is less than that of version2 or vice-versa, example: version1 = 1.1.2, version2 = 1.1.2.1

Test Cases:
1. version1 = 1.0, version2 = 2.0 ; return -1
2. version1 = 1.0, version2 = 1.0 ; return 0
3. version1 = 1.1.0, version2 = 1.01.1 ; return -1
4. version1 = 1.0.1, version2 = 1.1.1 ; return -1
5. version1 = 1.1.2, version2 = 1.1.2.1 ; return -1
6. version1 = 1.2.3, version2 = 1.2.1 ; return 1
7. version1 = 1.0, version2 = 1.0.0 ; return 0
8. version1 = 1.0.1, version2 = 1.0.2 ; return -1

Approaches:
1. Brute Force :: Two/Three Passes
Intuition:
Split the version string based on dot(it is now in a list). Convert list to integers and then, compare them. We can have zeros towards the end and need to avoid them so better, we delete/pop or add more zeros to equal versions' list's length, before proceeding with the solution.
Time: O(n + m) iterating over the whole input versions
Space: O(n + m) if considering the list of integers formed from versions given

2. Optimised :: Single Pass
Intuition:
Iterate over the version strings and get the chunk between two dots and compare them.
Time: O(max(n, m)) we will compare until we reach end of longest version length
Space: O(max(n, m)) we need substring of input for converting it to integer, string slice takes this space
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        length1, length2 = len(version1), len(version2)
        index1 = index2 = 0
        while index1 < length1 or index2 < length2:
            index1, version1_num = self.get_chunk(version1, index1, length1)
            index2, version2_num = self.get_chunk(version2, index2, length2)
            if version1_num != version2_num:
                return -1 if version1_num < version2_num else 1
        
        # versions are equal
        return 0
    
    def get_chunk(self, version, index, length):
        if index >= length:
            return index, 0
        
        index_end = index
        num = ''
        while index_end < length and version[index_end] != '.':
            num += version[index_end]
            index_end += 1
        num = int(num)
        index = index_end + 1
        return index, num
        
        
        
        
        
        
        
        
        """
        version1_list = list(map(int, version1.split('.')))
        version2_list = list(map(int, version2.split('.')))
        equal_count = 0
        index1, index2 = len(version1_list)-1, len(version2_list)-1
        while (index1 > -1):
            if version1_list[index1] == 0:
                version1_list.pop()
                index1 -= 1
            else:
                break
        while index2 > -1:
            if version2_list[index2] == 0:
                version2_list.pop()
                index2 -= 1
            else:
                break
        # print(version1_list, version2_list)
        index1 = index2 = 0
        while (index1 < len(version1_list) 
               and index2 < len(version2_list)):
            if version1_list[index1] < version2_list[index2]:
                return -1
            elif version1_list[index1] > version2_list[index2]:
                return 1
            elif version1_list[index1] == version2_list[index2]:
                equal_count += 1
            index1 += 1
            index2 += 1
        
        if index1 < len(version1_list):
            # version1 is greater than version2
            return 1
        if index2 < len(version2_list):
            # version2 is greater than version1
            return -1
        if equal_count == len(version1_list) == len(version2_list):
            return 0
        """