class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = {}
        arr1 = {}
        for items in s:
            if items in arr:
                arr[items] +=1
            else:
                arr[items] = 1
        for items in t:
            if items in arr1:
                arr1[items] += 1
            else:
                arr1[items] = 1

        if arr == arr1:
            return True
        else:
            return False
        
        