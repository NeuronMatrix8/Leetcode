class Solution:
    def heightChecker(self, heights: List[int]) -> int:
      count = 0 #initialise a counter
      for i in range(len(heights)):
        expected = sorted(heights) # Need to use sorted for array creation, not .sort(). That would sort the array heights in-place. 
        if heights[i] != expected[i]:
          count += 1
      return count
