class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #HashMap: {"a": 0 , "b": 1, "c":2}
        
        #L,R pointer 
        #"lecabee" L - l, R -e, 

        #"aab" : 'asjhdasab'


        if len(s1) > len(s2):
            return False

        hashMap = {}
        for i in range(len(s1)):
            if s1[i] not in hashMap:
                hashMap[s1[i]] =1 
            else:
                hashMap[s1[i]] +=1 
        l = 0
        r = len(s1)

        while r-1 < len(s2):
            hashMap2 = {}
            for j in range(l,r):
                if s2[j] not in hashMap2:
                    hashMap2[s2[j]] =1 
                else:
                    hashMap2[s2[j]] +=1 

            if hashMap == hashMap2:
                return True
        
            r+=1
            l+=1
        return False








        