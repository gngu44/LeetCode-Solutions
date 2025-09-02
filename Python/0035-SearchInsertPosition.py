class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low  = 0
        high = len(nums) - 1

        while (high >= low):
            mid = low + (high - low) // 2
            if (target == nums[mid]):
                return mid
            elif (target < nums[mid]):
                high = mid - 1
            else:
                low = mid + 1
        return low
        