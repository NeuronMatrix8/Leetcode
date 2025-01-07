class Solution:
    def findNumbers(self, nums: List[int]) -> int:
      count = 0 #initialise the counter
      for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0:
          count += 1
        else:
          i += 1
      return count

# Disclaimer : not the optimal way but can be solved by this
