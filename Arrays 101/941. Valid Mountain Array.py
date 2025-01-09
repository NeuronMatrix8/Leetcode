class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

      # first case 
      if len(arr) < 3:
        return False
      # traversing to find the peak 
      while i + 1 < len(arr) and arr[i+1] > arr[i]:
        i += 1 

      # check if the peak is the first or the last element 
      if i == arr[0] or i == len(arr) - 1:
        return False


    # traversing don from the peak 
    while i + 1 < len(arr) and arr[i] > arr[ i + 1]:
      i += 1

    return i == len(arr) - 1 
