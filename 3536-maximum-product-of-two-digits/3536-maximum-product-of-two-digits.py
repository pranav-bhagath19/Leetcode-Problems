class Solution(object):
    def maxProduct(self, n):
        temp = n
        ans = 0
        digits = []

        while temp != 0:
            digits.append(temp % 10)
            temp //= 10

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                ans = max(ans, digits[i] * digits[j])

        return ans