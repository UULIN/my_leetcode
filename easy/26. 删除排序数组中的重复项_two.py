def removeDuplicates(self, nums: List[int]) -> int:
    start, end =0, 1
    
    while start <= end and end < len(nums):
        if nums[start] == nums[end]:
            nums.pop(end)
        else:
            start = end
            end += 1
        
    return len(nums)