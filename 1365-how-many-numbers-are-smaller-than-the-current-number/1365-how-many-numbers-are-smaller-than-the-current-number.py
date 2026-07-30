class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans=[]
        for i in nums:
            sum=0
            for j in nums:
                if(i>j and j!=i):
                    sum+=1
            ans.append(sum)
        return ans
        