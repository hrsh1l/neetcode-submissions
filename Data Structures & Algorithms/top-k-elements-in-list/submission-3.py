from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            counts[nums[i]] += 1
        for num, cnt in counts.items():
            freq[cnt].append(num)

        #1:1, 2:2, 3:3

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        







            

        
            
                




        

    
        