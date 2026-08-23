class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} #Index: Value
        for i in range(0, len(strs)):
            value = ''.join(sorted(strs[i]))
            if value in map:
                map[value].append(strs[i])
            else:
                map[value] = [strs[i]]
        return list(map.values())

        