# https://leetcode.com/problems/course-schedule/


from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i: [] for i in range(numCourses)}
        for c1, c0 in prerequisites:
            courses[c0].append(c1)

        def is_cycle(c, visited):
            visited[c] = 1
            for next_c in courses[c]:
                if visited[next_c] == 1:
                    return True
                if visited[next_c] == 0:
                    if is_cycle(next_c, visited):
                        return True

            visited[c] = 2
            return False

        visited = [0]*numCourses
        for c in range(numCourses):
            if visited[c] == 0:
                if is_cycle(c, visited):
                    return False
        return True



if __name__ == '__main__':
    numCourses = 20
    prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    print(Solution().canFinish(numCourses, prerequisites))
