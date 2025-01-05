class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0 #initialise the variable sum
        for i in range(len(nums)): # Traversing nums 
            sum += nums[i] 
            nums[i] = sum
        return nums
