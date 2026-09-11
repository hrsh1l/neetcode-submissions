class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #"zxyzxyz"
        #L = Z
        #R = X
        #Calculate the ascii vals of l,r r should be +1 of l
        #variable sliding window do r+1
        #else l goes to r, and r+1 and recalc

        hashSet = set()
        l = 0
        maxCount = 0

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])         # remove something from hashSet
                l+=1        # move l forward

            hashSet.add(s[r])             # add s[r] to hashSet, now that duplicates are cleared
            maxCount = max(maxCount, (r-l)+1)   # what's the window size here?

        return maxCount


            



            
        



            
        

        
        