class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
      arr1 = [] #create a new array
      for i in range(len(arr)):
        if arr[i] == 0:
          arr1.append(arr[i])
          arr1.append(0)
        else:
          arr1.append(arr[i])
      for i in range(len(arr)):
        arr[i] = arr1[i]
