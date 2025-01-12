class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      arr1 = []
      nums_1 = set(nums) # To avoid Time Limit exceeded error.
      n = len(nums)
      for i in range(n):
        if i not in nums_1:
          arr1.append(i)
      return arr1


# Using additional space sol. 
