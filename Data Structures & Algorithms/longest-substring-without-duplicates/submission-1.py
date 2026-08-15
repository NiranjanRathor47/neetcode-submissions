class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = ""
        max_len = 0
        for i in range(n):
            if s[i] not in ans:
                ans += s[i]
            else:
                ans = ans[ans.find(s[i]) + 1:] + s[i]
            max_len = max(len(ans),max_len)
        return max_len
