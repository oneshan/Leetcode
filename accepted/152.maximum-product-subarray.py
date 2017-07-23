#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray
#
# Medium (25.37%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-2]'
#
#
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
#
#
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
#
#


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        ans, currMax, currMin = float('-inf'), 1, 1
        for num in nums:
            currMax *= num
            currMin *= num
            currMax, currMin = max(currMax, currMin, num), min(currMax, currMin, num)
            ans = max(ans, currMax)
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 3, -2, 4]
    print(sol.maxProduct(arr))
