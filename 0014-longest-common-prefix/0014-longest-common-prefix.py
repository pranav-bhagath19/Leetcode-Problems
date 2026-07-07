class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        strs.sort()
        f, l, i = strs[0], strs[-1], 0
        while i < len(f) and i < len(l) and f[i] == l[i]:
            i += 1
        return f[:i]
