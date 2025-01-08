class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

  for i in range(m):
    arr.append(nums1[i])
  for j in range(n):
    arr.append(nums1[j])
  arr.sort()
  for k in range(m+n):
    nums1[k] = arr[k]


# Not an optimal solution but a brute force approach 
