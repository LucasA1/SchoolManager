from datetime import date
from models import User, Course, Assignment, Basic_Relationship, \
    get_course_grade, get_course_assignments, get_course_messages, update_assignment_grade, get_student_assignments


def create_user(username, password, user_id, user_type, firstname, lastname, email):
    new_user = User(username, user_id, user_type, firstname, lastname, email)
    User.register(new_user, password)


def create_course(course_name, credits, description):
    new_course = Course(course_name, credits, description)
    Course.create_course(new_course)


def create_relationship(year, semester, username, course_name):
    rel = Basic_Relationship()
    Basic_Relationship.create_student_course_rel(rel, username, course_name, semester, year)


def create_assignment(assignment_name, date_due, points, description):
    new_assignment = Assignment(assignment_name, date_due, points, description)
    Assignment.create_assignment(new_assignment)


def create_s_a_rel(username, assignment_name, date_assigned):
    rel = Basic_Relationship()
    Basic_Relationship.create_student_assignment_rel(rel, username, assignment_name, date_assigned)


def create_c_a_rel(coursename, assignment_name, date_posted):
    rel = Basic_Relationship()
    Basic_Relationship.create_assignment_course_rel(rel, coursename, assignment_name, date_posted)

def update_grades(username, assignment_name, course_name, grade):
    update_assignment_grade(username, assignment_name, course_name, grade)

def get_grades(username, coursename):
    rels = get_course_grade(username, coursename)

def get_assignments(username):
    rels = get_student_assignments(username)
    for rel in rels:
        print(rel)

"""
Creates a sample of users for database
"""
create_user("Bob", "1234", "123456789", "student", "Bob", "Ross", "bob.ross@gmail.com")
create_user("jack1", "password", "420937538", "student", "Jack", "Roberts", "jack1@iastate.edu")
create_user("joe23", "abc123", "875263788", "teacher", "Joe", "Smith", "joe23.smith@gmail.com")
create_user("tyler47", "!password!", "098987652", "student", "Tyler", "Anderson", "tyler47.anderson@gmail.com")
create_user("emma14", "a667gh!", "100981234", "teacher", "Emma", "Roberts", "emma14.roberts@gmail.com")

"""
Creates sample of courses in database
"""
create_course("MIS_407", 3, "Python")
create_course("MIS_320", 3, "Database")
create_course("MIS_340", 3, "Project Management")

"""
Creates sample relationship between user(student) and course
"""
create_relationship(2017, "Fall", "Bob", "MIS_407")
create_relationship(2017, "Fall", "jack1", "MIS_407")
create_relationship(2017, "Fall", "joe23", "MIS_407")
create_relationship(2017, "Fall", "tyler47", "MIS_407")
create_relationship(2017, "Fall", "Bob", "MIS_320")
create_relationship(2017, "Fall", "jack1", "MIS_320")
create_relationship(2017, "Fall", "joe23", "MIS_320")
create_relationship(2017, "Fall", "tyler47", "MIS_320")
create_relationship(2017, "Fall", "Bob", "MIS_340")
create_relationship(2017, "Fall", "jack1", "MIS_340")
create_relationship(2017, "Fall", "joe23", "MIS_340")
create_relationship(2017, "Fall", "tyler47", "MIS_340")

"""
Creates sample assignments
"""
create_assignment("HW_01", "12/14/17", 60.0, "HW number 1")
create_assignment("HW_02", "12/14/17", 70.0, "HW number 2")
create_assignment("HW_03", "12/14/17", 80.0, "HW number 3")


"""
Creates student to assignment relationship
"""
create_s_a_rel("Bob", "HW_01", "12/14/17")
create_s_a_rel("jack1", "HW_01", "12/14/17")
create_s_a_rel("joe23", "HW_01", "12/14/17")
create_s_a_rel("tyler47", "HW_01", "12/14/17")
create_s_a_rel("Bob", "HW_02", "12/14/17")
create_s_a_rel("jack1", "HW_02", "12/14/17")
create_s_a_rel("joe23", "HW_02", "12/14/17")
create_s_a_rel("tyler47", "HW_02", "12/14/17")
create_s_a_rel("Bob", "HW_03", "12/14/17")
create_s_a_rel("jack1", "HW_03", "12/14/17")
create_s_a_rel("joe23", "HW_03", "12/14/17")
create_s_a_rel("tyler47", "HW_03", "12/14/17")


"""
Creates assignment to course relationship
"""
create_c_a_rel("MIS_407", "HW_01", "12/14/17")
create_c_a_rel("MIS_407", "HW_02", "12/14/17")
create_c_a_rel("MIS_320", "HW_03", "12/14/17")


update_grades("Bob", "HW_01", "MIS_407", 40)
update_grades("jack1", "HW_01", "MIS_407", 45)
update_grades("joe23", "HW_01", "MIS_407", 50)
update_grades("tyler47", "HW_01", "MIS_407", 60)
update_grades("Bob", "HW_02", "MIS_407", 60)
update_grades("jack1", "HW_02", "MIS_407", 70)
update_grades("joe23", "HW_02", "MIS_407", 40)
update_grades("tyler47", "HW_02", "MIS_407", 45)
update_grades("Bob", "HW_03", "MIS_407", 80)
update_grades("jack1", "HW_03", "MIS_407", 75)
update_grades("joe23", "HW_03", "MIS_407", 60)
update_grades("tyler47", "HW_03", "MIS_407", 50)


"""
Tests add_post()
Must create a node with a Title and Text as well as have attributes applied by timestamp() and date().
Must also create relationship to corresponding user.
"""
# created_user = User("Bob", "123456789", "Bob", "Ross", "bob.ross@gmail.com")
# User.add_post(created_user, "Title", "Text")
#
# """
# Tests for verify_password()
# """
# password = "1234"
# created_user = User("Bob", "123456789", "Bob", "Ross", "bob.ross@gmail.com")
# User.verify_password(created_user, password)
#
# """
# Tests deleting a user
# """
# User.delete_user('Bob')
