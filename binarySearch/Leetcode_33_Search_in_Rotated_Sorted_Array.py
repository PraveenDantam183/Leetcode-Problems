class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2
                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]: return mid
                if mid - 1 >= 0 and nums[mid] < nums[mid - 1]: return mid - 1
                if nums[mid] < nums[0]: right = mid - 1
                else: left = mid + 1 
            return -1

        def search(left, right):
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target: return mid
                elif target < nums[mid]: right = mid - 1
                else: left = mid + 1
            return -1

        pivot = find_pivot()
        print(pivot)
        if pivot == -1: return search(0, len(nums) - 1)
        if target == nums[pivot]: return pivot
        if target < nums[0]: return search(pivot + 1, len(nums) - 1)
        return search(0, pivot - 1)
