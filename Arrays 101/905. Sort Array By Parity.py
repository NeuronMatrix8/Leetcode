class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
      l = 0
      for i in range(len(nums)):
        if nums[i] == 0:
          nums[l], nums[i] = nums[i], nums[l]
          l += 1
