# LeetCode 347: 前 K 个高频元素 (Top K Frequent Elements)
#
# 题目：找出数组中出现频率最高的前 k 个元素。
#
# 核心思路（桶排序 / Bucket Sort）：
# 1. 先用哈希表统计每个元素的出现频率。
# 2. 再用"桶"按频率归类：buckets[freq] 存放所有出现 freq 次的元素。
#    （桶的下标就是频率，所以桶的数量 = 数组长度 + 1，因为最高频率不超过 n）
# 3. 从高频到低频遍历桶，收集元素，直到凑满 k 个。
#
# 为什么用桶排序而不是直接排序？
#   直接排序 O(n log n)；桶排序利用"频率范围有限（0~n）"这个特性，做到 O(n)。
#
# 例如：nums = [1,1,1,2,2,3], k=2
#   频率表：1→3次, 2→2次, 3→1次
#   桶：buckets[1]=[3], buckets[2]=[2], buckets[3]=[1]
#   从高频到低频：i=3→[1], i=2→[2]，凑满 2 个 → 返回 [1, 2]
#
# 时间复杂度：O(n)——统计 O(n) + 建桶 O(n) + 收集 O(n)
# 空间复杂度：O(n)——哈希表 + 桶

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]   # 出现频率最高的前 k 个元素
    """
    # 第1步：统计每个元素的出现频率
    freq_map = {}
    for n in nums:
        freq_map[n] = freq_map.get(n, 0) + 1

    # 第2步：建桶，桶的下标 = 频率
    # 长度为 n+1，因为单个元素最多出现 n 次
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_map.items():   
        buckets[freq].append(num)

    # 第3步：从高频到低频收集，直到凑满 k 个
    res = []
    for i in range(len(buckets) - 1, 0, -1):   # len(buckets)-1 而非 len((buckets)-1)
        for num in buckets[i]:                 # 遍历桶内元素
            res.append(num)
            if len(res) == k:                  # 凑满 k 个就返回
                return res

    return res
