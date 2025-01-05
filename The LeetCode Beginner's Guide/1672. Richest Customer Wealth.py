class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0 #initialize wealth to zero
        for i in range(len(accounts)):
            totalWealth = sum(accounts[i]) #calculating each customer's wealth 
            maxWealth = max(maxWealth, totalWealth) #returning the maximum wealth
        return maxWealth
