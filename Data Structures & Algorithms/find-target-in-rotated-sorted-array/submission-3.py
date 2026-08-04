class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l = 0 
        r = len(nums) - 1
        rotations = 6
        while l <= r:
            m = (l + r) // 2
            if (m == 0 and nums[m + 1] > nums[m]) or nums[m - 1] > nums[m]:
                rotations = m
                break
            else:
                if nums[r] < nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        l = 0 
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if m < rotations:
                if nums[l] > target:
                    l = m + 1
                else:
                    if nums[m] > target:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                if nums[r] < target:
                    r = m - 1
                else:
                    if nums[m] > target:
                        r = m - 1
                    else:
                        l = m + 1
        return -1