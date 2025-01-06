class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      #convert magazine into a list 
      magazine_list = list(magazine) 
      if len(ransomNote) > len(magazine): # if length of ransomNote is greater than magazine, return False
        return False
      for char in ransomNote:
        if char in magazine_list:
          magazine_list.remove(char)
        else:
          return False
      return True    
