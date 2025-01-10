lass Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 # intialise a pointer
        for i in range(len(nums)):
          if nums[i] != 0 :
            nums[l], nums[i] = nums[i], nums[l] # swap if not zero
            l += 1
            
