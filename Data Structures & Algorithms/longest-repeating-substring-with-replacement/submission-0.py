from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Check the character w most freq against sliding window. If window Length - maxFrequency = replacementNeeded
        #Check this value against
        #Sliding window - from start, and keep going, and shrink from left once k is greater than replacementNeeded
        #Store maxCount ...

        # A A A B A B K =1

        count = defaultdict(int)
        left = 0
        maxLength = 0
        maxFrequency = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            maxFrequency = max(maxFrequency, count[s[right]])

            while (right - left + 1) - maxFrequency > k:
                count[s[left]] -=1
                left +=1
            
            maxLength = max(maxLength, right-left + 1)

        return maxLength




            



        