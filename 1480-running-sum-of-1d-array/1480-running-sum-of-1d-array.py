class Solution(object):
    def runningSum(self, nums):
        runningsum=[]
        runningsum.append(nums[0])
        for i in range(1,len(nums)):
            runningsum.append(nums[i]+runningsum[i-1])
        return runningsum
        