class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        adjlist = defaultdict(set)
        cntr = [0] * numCourses
        courses = 0
        for course, prereq in prerequisites:
            adjlist[prereq].add(course)
            cntr[course] += 1 
        for i in range(len(cntr)):
            if cntr[i] == 0:
                q.append(i)
        while q:
            courseTaken = q.popleft()
            courses += 1 
            for course in adjlist[courseTaken]:
                cntr[course] -= 1
                if cntr[course] == 0:
                    q.append(course)
        if courses == numCourses:
            return True
        else:
            return False


        