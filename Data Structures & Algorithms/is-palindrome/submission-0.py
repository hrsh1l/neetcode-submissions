import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        n = len(s)
        for i in range(0,n):
            j = n - 1 -i
            if s[i] != s[j]:
                return False
            if i == j or i > j:
                return True
        return True

        