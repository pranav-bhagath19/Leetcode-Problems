class Solution(object):
    def smallestNumber(self, n, t):
         while True:
            prod = 1
            temp = n 
            while temp > 0:
                digit = temp % 10
                prod *= digit
                temp //= 10
            if prod % t == 0:
                return n
            
            n += 1
        