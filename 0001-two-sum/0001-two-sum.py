class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary to store value and its index
        
        for index, value in enumerate(nums):
            complement = target - value
            
            if complement in num_map:
                return [num_map[complement], index]
            
            num_map[value] = index  # Store index of the current number
        
        return []  # Return empty list if no solution is found (shouldn't happen as per problem constraints)
