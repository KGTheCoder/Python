class Solution:
    def missingNumber(self, nums):

        # Arrange nums in ascending order 
        nums.sort()

        # If the last value in nums is not equal to the length of nums,
        if nums[-1] != len(nums):

            # Return the length of nums 
            return len(nums)

        # Else, if the first value of nums is not equal to 0,    
        elif nums[0] != 0:

            # Return 0
            return 0
        
        # For every value in the range of 1 to the length of nums,
        for i in range(1, len(nums)):

            # Expected_num is equal to nums at nums[i-1] + 1
            expected_num = nums[i-1] + 1

            # If nums at i is not equal to expected_num,
            if nums[i] != expected_num:

                # Return expected_num
                return expected_num

solution = Solution()
nums = [3, 0, 1]
print(solution.missingNumber(nums))