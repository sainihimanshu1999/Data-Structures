'''
we have to return the list of courses arranges in how they should be studied
'''

def courseSchedule(numCourses,prerequest):
    source = [set() for _ in range(numCourses)]
    destination = [set() for _ in range(numCourses)]

    for d,s in prerequest:
        source[d].add(s)
        destination[s].add(d)


    result = [x for x in range(numCourses) if not source[x]]

    for i in result:
        for d in destination[i]:
            source[d].remove(i)
            if not source[d]:
                result.append(d)

    return result if len(result)==numCourses else []