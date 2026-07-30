class Solution(object):
    def dominantIndex(self, nums):
        largest=float("-inf")
        second=float("-inf")
        largestIndex = -1
        for i,num in enumerate(nums):
            if num>largest:
                second=largest
                largest=num
                largestIndex = i
            elif num>second:
                second=num
        if(largest>=2*second):
            return largestIndex
        else:
            return -1


        