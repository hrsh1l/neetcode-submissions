class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] +=1
            else:
                counts[i] = 1

        sortedKeys = sorted(counts, key=counts.get, reverse=True)

        return sortedKeys[:k]
        
        
            
                




        

    
        