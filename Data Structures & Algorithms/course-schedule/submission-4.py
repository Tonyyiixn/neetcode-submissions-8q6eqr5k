class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i) 
        
        courses_taken = 0
        while queue:
            curr = queue.popleft()
            courses_taken += 1
            for course in graph[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return courses_taken == numCourses