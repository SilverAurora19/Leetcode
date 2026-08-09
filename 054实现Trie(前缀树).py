# LeetCode 208: 实现 Trie（前缀树）(Implement Trie (Prefix Tree))
#
# 前置知识——什么是 Trie？
# Trie（前缀树 / 字典树）是一种 N 叉树，专门用来高效存储和查找字符串集合。
# 核心思想：共享公共前缀——有相同前缀的字符串共用同一条路径。
#
# 例如插入 "app", "apple", "bat" 后，树的结构：
#
#         root
#        /    \
#       a      b
#       |      |
#       p      a
#       |      |
#       p(is)  t(is)
#       |
#       l
#       |
#       e(is)
#
#   is = is_end = True，表示从根到该节点的路径是一个完整单词
#   搜索 "app" → 走 a→p→p，最后 is_end=True → True
#   搜索 "ap"  → 走 a→p，但 p 的 is_end=False → False
#   前缀 "ap"  → 走 a→p，节点存在 → True
#
# 为什么不用哈希表？
#   - 哈希表无法高效查"前缀"（startsWith）
#   - 哈希表每个单词独立存储，无法共享前缀，内存大
#
# 时间复杂度：
#   insert / search / startsWith：O(k)，k 为字符串长度（与存了多少单词无关！）
# 空间复杂度：O(N × k × 26) 最坏情况，实际远小（共享前缀）

# ===== Trie 节点 =====
class TrieNode(object):
    def __init__(self):
        # children：字符 → 子节点 的映射
        # 用字典而非定长数组（26），更灵活，不限于小写字母
        self.children = {}
        # is_end：从根走到当前节点，是否构成一个完整单词
        # True = 是一个单词的结尾（例如 "app" 的最后一个 p）
        self.is_end = False


class Trie(object):

    def __init__(self):
        # 根节点是空节点，不存字符，只作为入口
        self.root = TrieNode()

    def insert(self, word):
        """
        插入单词：从根出发，逐字符向下走，没有对应子节点就创建。
        最后把终点节点的 is_end 标为 True。
        :type word: str
        :rtype: None
        """
        node = self.root

        for char in word:
            # 当前字符还没有对应子节点 → 创建一个
            if char not in node.children:
                node.children[char] = TrieNode()

            # 沿着子节点继续往下走
            node = node.children[char]

        # 走到单词最后一个字符，标记"这是一个完整单词"
        node.is_end = True

    def search(self, word):
        """
        搜索完整单词：必须完全匹配，且最后节点 is_end=True。
        :type word: str
        :rtype: bool
        """
        node = self.root

        for char in word:
            # 中途字符无法匹配 → 单词不存在
            if char not in node.children:
                return False

            node = node.children[char]

        # 走到最后了，检查这个位置是否标记为完整单词
        # 例如：插入了 "apple"，查 "app" → 节点存在但 is_end=False → False
        return node.is_end

    def startsWith(self, prefix):
        """
        搜索前缀：不需要 is_end=True，只要能走到最后节点就行。
        :type prefix: str
        :rtype: bool
        """
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        # 能顺利走完前缀的所有字符 → 存在以该前缀开头的单词
        return True
