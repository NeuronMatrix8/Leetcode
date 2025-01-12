class Solution:
    def thirdMax(self, nums: List[int]) -> int:
      arr1 = []   # Creating a new array
      for i in nums:
        if i not in arr1:
          arr1.append(i)
      arr1.sort()
      if len(arr1) < 3:
        return max(arr1) # Handling the edge case
      return arr[-3] # returning the third max element of the array. Note:  indexing from last. 

# Disclaimer - Not an optimal T.C and S.C. 
