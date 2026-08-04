class Solution(object):
    def findMissingElements(self, a):
        full_range = set(range(min(a), max(a) + 1))
        unique_elements = set(a)
        missing_elements = full_range.difference(unique_elements)
        result = sorted(missing_elements)

        return result