class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mydeq = deque()
        for i in range(k):
            while mydeq and mydeq[len(mydeq) - 1] < nums[i]:
                mydeq.pop()
            mydeq.append(nums[i])
        print(mydeq)
        arr = []
        arr.append(mydeq[0])
        left = 0 
        right = left + k
        while right < len(nums):
            if mydeq[0] == nums[left]:
                mydeq.popleft()
            left += 1
            while mydeq and mydeq[len(mydeq) - 1] < nums[right]:
                mydeq.pop()
            mydeq.append(nums[right])
            arr.append(mydeq[0])
            right += 1
        return arr