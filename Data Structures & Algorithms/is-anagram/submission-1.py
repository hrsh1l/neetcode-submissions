class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [""]
        arr1 = [""]
        for items in s:
            if items != arr:
                arr.append(items)
        for items in t:
            if items != arr1:
                arr1.append(items)
        
        arr.sort()
        arr1.sort()

        if arr == arr1:
            return True
        else:
            return False

        
        