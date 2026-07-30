class Solution(object):
    def thirdMax(self, nums):
        largest = float("-inf")
        second = float("-inf")
        third = float("-inf")

        for current in nums:
            if current == largest or current == second or current == third:
                continue
            if current>largest:
                third=second
                second = largest
                largest = current
            elif current>second and current!=largest:
                third = second
                second= current
            elif current>third:
                third=current
            
        if(third == float("-inf")):
                return largest
        return third
                

