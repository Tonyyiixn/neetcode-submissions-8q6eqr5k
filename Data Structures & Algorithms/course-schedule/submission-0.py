class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        Indegree = [0]* numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            Indegree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if Indegree[i] == 0:
                queue.append(i)
        
        Courses_passed = 0
        
        while queue:
            curr = queue.popleft()
            Courses_passed += 1

            for course in graph[curr]:
                Indegree[course] -= 1
                if Indegree[course] == 0:
                    queue.append(course)
        

        return Courses_passed == numCourses