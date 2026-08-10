class Solution:
    def arraySum(self, arr):
        total = 0
        for num in arr:
            total += num
        return total
    
sol = Solution()
arr = [1, 2, 3, 4, 5]
result = sol.arraySum(arr)
print("The sum of the array is:", result)