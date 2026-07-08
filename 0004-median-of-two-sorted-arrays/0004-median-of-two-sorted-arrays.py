class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        new = nums1 + nums2
        new.sort()
        x = len(new)
        y = x // 2
        if x % 2 == 0:
            median = (new[y - 1] + new[y]) / 2.0
        else:
            median = new[y]
        return median