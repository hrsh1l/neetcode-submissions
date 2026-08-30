class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i not in hashMap:
                stack.append(i)
            else:
                if not stack:
                    return False
                
                if hashMap[i] == stack.pop():
                    continue
                else:
                    return False
        return len(stack)==0
            