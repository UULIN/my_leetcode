
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    list_result = []
    nums.sort()
    num_len = len(nums)
    for i in range(num_len):
        # 如果第一个数大于0，则不存在三数之和小于0，直接退出
        if nums[i] > 0:
            break
        # 如果两个数相等，则略过，进入下一次循环
        if i > 0 and nums[i] == nums[i -1]:
            continue
        # 记录i的下一个数的位置
        j = i + 1
        # 记录最后一个数的位置
        k = num_len - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                list_result.append([nums[i], nums[j], nums[k]])
            # 判断相邻元素是否相等，相等则跳过
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                # 没有相等的则进行缩小范围
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
    return list_result


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))