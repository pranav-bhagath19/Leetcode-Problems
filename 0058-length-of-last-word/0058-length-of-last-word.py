class Solution(object):
    def lengthOfLastWord(self, s):
        length=0
        a=s[::-1]
        for char in a:
            if char == " ":
                if length > 0: 
                    break
                else:  
                    continue
            else:
                length += 1
        return length
        