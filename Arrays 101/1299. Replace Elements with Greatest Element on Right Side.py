class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
      max_val = -1 # for last place replacement
      for i in range(n-1, -1, -1):  # key here is reverse traversal
        current = arr[i]
        arr[i] = max_val
        max_val = max(current, max_val)
      return arr
