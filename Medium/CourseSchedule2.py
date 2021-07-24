'''We will do this graph question using topological sort and topological sort return false when there will be cycle'''

from collections import defaultdict

def courseSchedule(numCourses, prerequisties):

    graph = defaultdict(list)

    for u,v in prerequisties:
        graph[u].append(v)

    result = []

    visited,cycle = set(),set()


    def dfs(course):

        if course in cycle:
            return False

        if course in visited:
            return True

        cycle.add(course)

        for preq in graph[course]:
            if dfs(preq) == False:
                return False

        cycle.remove(course)

        visited.add(course)

        result.append(course)

        return True


    for c in range(numCourses):
        if dfs(c) == False:
            return []

    return result


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

print(courseSchedule(numCourses,prerequisites))