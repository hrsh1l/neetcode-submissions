class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #We first want to count the number of occurences in the string
        counts = {}

        #Initialise an empty array, with the different value bucket pairs
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)

        #For each number, count within the hashmap, add it to the array
        for n,c in counts.items():
            freq[c].append(n)
        result = []
        for i in range(len(freq)-1, 0, -1):
            #We do this inner loop because we don't know there may be multiple occurences in the same bucket
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
            

        
            
                




        

    
        