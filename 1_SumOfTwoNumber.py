
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 在进行迭代并将元素插入到表中的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。
# 如果它存在，那我们已经找到了对应解，并立即将其返回。

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_dict={}
        for i in range(len(nums)):
            if target-nums[i] in new_dict:
                return [new_dict[target-nums[i]],i]
            else:
                new_dict[nums[i]]=i


if __name__== "__main__":
    nums=[2,7,11,15]
    target=9
    test=Solution()
    result=test.twoSum(nums,target)
    print(result)

# 复杂度分析：
#
# 时间复杂度：O(n)， 我们只遍历了包含有n个元素的列表一次。在表中进行的每次查找只花费 O(1)的时间。
#
# 空间复杂度：O(n)，所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存储 n 个元素。