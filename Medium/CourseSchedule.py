'''This is basic topological sort in graph'''

from collections import defaultdict

def courseSchedule(numCourses,prerequisties):

    graph = defaultdict(list)

    for u,v in prerequisties:
        graph[u].append(v)


    cycle = set()

    def dfs(course):

        if course in cycle:
            return False

        if graph[course] == []:
            return True

        cycle.add(course)

        for preq in graph[course]:
            if dfs(preq) == False:
                return False

        cycle.remove(course)

        graph[course] = []

        return True


    for c in range(numCourses):
        if dfs(c) == False:
            return False

    return True


numCourses = 2
prerequisites = [[1,0]]

print(courseSchedule(numCourses,prerequisites))

