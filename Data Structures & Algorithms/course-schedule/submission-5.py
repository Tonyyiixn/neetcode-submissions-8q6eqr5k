class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        courses_passed = 0
        while queue:
            curr_cour = queue.popleft()
            courses_passed += 1
            for course in graph[curr_cour]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return courses_passed == numCourses