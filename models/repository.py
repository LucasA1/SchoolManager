from py2neo import authenticate, Graph

authenticate('localhost:7474', 'neo4j', 'A1b2c3d4')
graph = Graph('http://localhost:7474/db/data/')

def get_course_assignments(coursename):
    query = '''
             MATCH (course:Course)<-[:POSTED_TO]-(assignment:Assignment)
             WHERE course.course_name = {coursename}
             RETURN assignment
             '''
    assignments = graph.run(query, coursename=coursename).data()
    return assignments

def get_student_assignments(username):
    query = '''
                 MATCH (user:User)<-[:ASSIGNED_TO]-(assignment:Assignment)
                 WHERE user.username = {username}
                 RETURN assignment
                 '''
    assignments = graph.run(query, username=username).data()
    assignment_array = []
    for assignment in assignments:
        assignment_array.append(dict(assignment.get('assignment')))
    return assignment_array

def get_course_messages(coursename):
    query = '''
             MATCH (course:Course)<-[:TAGGED_TO]-(message:Message)
             WHERE course.course_name = {coursename}
             RETURN message
             '''
    messages = graph.run(query, coursename=coursename).data()
    return messages

"""
def get_course_grade(username, coursename):
    query = '''
             MATCH (course:Course)<-[rel1:POSTED_TO]-(assignment:Assignment)-[rel2:ASSIGNED_TO]->(user:User)
             WHERE user.username = {username}
             AND course.course_name = {coursename}
             AND rel2.grade IS NOT NULL
             RETURN rel2, course, assignment
             '''
    results = graph.run(query, username=username, coursename=coursename)
    grades =[]
    for result in results.data():
        grade = result.get('rel2')['grade']
        total_points = result.get('rel2')['total_points']
        if grade and total_points:
            assignment_grade = ((grade/total_points) * 100)
            course = result.get('course')
            assignment = result.get('assignment')
            result_dict = {'course_name': course['course_name'],
                           'assignment_name': assignment['assignment_name'], 'grade': round(assignment_grade, 2)}
            grades.append(result_dict)
    return grades
"""

def get_course_grade(username):
    query = '''
             MATCH (course:Course)<-[rel1:POSTED_TO]-(assignment:Assignment)-[rel2:ASSIGNED_TO]->(user:User)
             WHERE user.username = {username}
             AND rel2.grade IS NOT NULL
             RETURN rel2, course, assignment
             '''
    results = graph.run(query, username=username)
    grades =[]
    for result in results.data():
        grade = result.get('rel2')['grade']
        total_points = result.get('rel2')['total_points']
        if grade and total_points:
            assignment_grade = ((grade/total_points) * 100)
            course = result.get('course')
            assignment = result.get('assignment')
            result_dict = {'course_name': course['course_name'],
                           'assignment_name': assignment['assignment_name'], 'grade': round(assignment_grade, 2)}
            grades.append(result_dict)
    return grades

def get_student_course(username):
    query = '''
            MATCH (user:User)-[:TAKES]->(course:Course)
            WHERE user.username = {username}
            RETURN course
            '''
    temp_courses = graph.run(query, username=username).data()
    courses = []
    for course in temp_courses:
        courses.append(dict(course.get('course')))
    return courses

def update_assignment_grade(username, assignment_name,course_name, grade):
    query = '''
             MATCH (user:User)<-[rel:ASSIGNED_TO]-(assignment:Assignment)-[:POSTED_TO]->(course:Course)
             WHERE user.username = {username}
             AND assignment.assignment_name = {assignment_name}
             AND course.course_name = {course_name}
             WITH rel, assignment
             SET rel.grade = {grade}
             SET rel.total_points = assignment.points
             RETURN rel
             '''
    rel = graph.run(query, username=username, assignment_name=assignment_name, course_name=course_name, grade=grade).data()
    return rel
