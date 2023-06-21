# Name : Anish Banswada

# Time Taken : 35 mins

# Assumptions : No cycles

# Space Complexity : O(V+E)

# Time Complexity : O(V+E)

from collections import  deque

# Function 
def prerequisites(courses, course_map):
    indegree = {}
    for course in courses:
        course_map[course] = course_map.get(course,[])
        indegree[course] = indegree.get(course,0)
        for prereq in course_map[course]:
            indegree[prereq] = indegree.get(prereq,0) + 1
    queue = deque()
    for course in indegree:
        if indegree[course] == 0:
            queue.append(course)
    res = []
    while queue:
        cur_course = queue.popleft()
        res.append(cur_course)
        for prereq in course_map[cur_course]:
            indegree[prereq] -= 1
            if indegree[prereq] == 0:
                queue.append(prereq)
    return res[::-1]


# Main

if __name__ == "__main__":
    assert prerequisites(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
) == ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"]
    assert prerequisites(["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
) == ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Plays & Screenplays", "Comparative Literature"]
    print("Testing completed")
 