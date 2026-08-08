from collections import deque

# LeetCode 207: 课程表 (Course Schedule)
#
# 题目：有 numCourses 门课程，prerequisites 是前置条件列表，
# 例如 [1, 0] 表示要先修课程 0 才能修课程 1。
# 判断是否可能完成所有课程（即图中是否有环——有环则无法完成）。
#
# 核心思路（拓扑排序 / Kahn 算法 / BFS + 入度表）：
# 这本质是判断有向图是否包含环，用拓扑排序来做：
#   - 能把所有节点排完 → 无环 → True
#   - 排不完（有环的节点入度永远不会变成 0）→ 有环 → False
#
# 步骤：
# 1. 建图：graph[先修课] = [后修课列表]
# 2. 统计入度：indegree[课程] = 有几门前置课还没修
# 3. 所有入度为 0 的课程（不需要前置课）入队
# 4. BFS：每出队一个课程，把它指向的后续课程的入度 -1
#    如果某个后续课入度变成 0 → 入队（说明前置课全修完了）
# 5. 最后看修完的课程数是否等于总数
#
# 例如：numCourses = 4, prerequisites = [[1,0],[2,1],[3,2]]
#
#   建图：0 → 1 → 2 → 3（一条链，无环）
#   入度：[0, 1, 1, 1]
#
#   BFS：
#   初始入队：0（入度为 0）
#   弹 0 → 1 的入度 -1→0 → 1 入队 → completed=1
#   弹 1 → 2 的入度 -1→0 → 2 入队 → completed=2
#   弹 2 → 3 的入度 -1→0 → 3 入队 → completed=3
#   弹 3 → completed=4
#   4 == 4 → True
#
# 有环的例子：numCourses = 2, prerequisites = [[0,1],[1,0]]
#
#   建图：0 → 1, 1 → 0（互相依赖，有环）
#   入度：[1, 1]
#
#   BFS：
#   初始入队：无（没有入度为 0 的节点）
#   队列为空，completed=0
#   0 != 2 → False（有环，无法修完）
#
# 时间复杂度：O(V + E)——每个节点和边各处理一次
# 空间复杂度：O(V + E)——邻接表 + 入度数组 + 队列

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool   # 能否完成所有课程（图中无环）
        """
        # graph[i]：修完课程 i 之后可以修的课程列表（邻接表）
        graph = [[] for _ in range(numCourses)]

        # indegree[i]：课程 i 还剩几门前置课没修（入度）
        indegree = [0] * numCourses

        # 建图 + 统计入度
        # 边方向：prerequisite → course（先修课指向后修课）
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        q = deque()

        # 入度为 0 的课程（没有前置课，可以直接修）全部入队
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        completed = 0   # 已修完的课程数

        # BFS：按拓扑顺序逐个修课
        while q:
            course = q.popleft()
            completed += 1   # 修完当前课程

            # 把当前课程的所有"后续课程"的入度减 1
            # 如果某个后续课入度变成 0，说明它的前置课全修完了 → 入队
            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        # 修完的课程数 == 总数 → 无环，可以完成
        return completed == numCourses
