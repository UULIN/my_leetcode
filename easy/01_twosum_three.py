# 两数之和hashmap实现
def twoSum(nums, target):
    """
    :param nums:列表
    :param target: 目标值
    :return: 目标值两个的下标
    """
    hashmap = {}
    for i in range(len(nums)):
        m = nums[i]
        if target - m in hashmap:
            return hashmap[target - m], i # 如果目标值在hashmap中，则返回目标值下标和i的下标
        else:
            hashmap[m] = i # 如果不存在，则进行记录
if __name__ == '__main__':
    print(twoSum([2,3,1],3))
