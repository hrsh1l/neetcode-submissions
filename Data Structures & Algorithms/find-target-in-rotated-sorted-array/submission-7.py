class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or nums[left] > target: #Too big to be in left half or smaller than min val in left half
                    left = mid + 1
                else:
                    right = mid -1
            else:    
                if target < nums[mid] or nums[right] < target: #Too small to be in right half or larger than max val in right half
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


        
