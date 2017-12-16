from py2neo import authenticate, Graph, Relationship
import uuid
from datetime import datetime
from .user import User
from .course import Course
from .message import Message
from .assignment import Assignment

authenticate('localhost:7474', 'neo4j', 'A1b2c3d4')
graph = Graph('http://localhost:7474/db/data/')

class Basic_Relationship():

    def __init__(self):
        self.relationship_id = str(uuid.uuid4())


    def create_student_course_rel(self, username, course_name, semester, year):
        user = User.get_user(username)
        course = Course.get_course_by_name(course_name)
        if user and course:
            rel = Relationship(user, 'TAKES', course, relationship_id=self.relationship_id, semester=semester, year=year)
            graph.create(rel)
            return rel
        else:
            return None

    def create_teacher_course_rel(self, username, course_name, semester, year):
        user = User.get_user(username)
        course = Course.get_course_by_name(course_name)
        if user and course:
            rel = Relationship(user, 'TEACHES', course, relationship_id=self.relationship_id, semester=semester, year=year)
            graph.create(rel)
            return rel
        else:
            return None

    def create_user_message_rel(self, username, message_id):
        user = User.get_user(username)
        message = Message.get_message_by_id(message_id)
        if user and message:
            rel = Relationship(user, 'POSTS', message, relationship_id=self.relationship_id)
            graph.create(rel)
            return rel
        else:
            return None

    def create_message_course_rel(self, coursename, message_id):
        course = Course.get_course_by_name(coursename)
        message = Message.get_message_by_id(message_id)
        if message and course:
            rel = Relationship(message, 'TAGGED_TO', course, relationship_id=self.relationship_id)
            graph.create(rel)
            return rel
        else:
            return None

    def create_student_assignment_rel(self, username, assignment_name, date_assigned):
        assignment = Assignment.get_assignment_by_name(assignment_name)
        user = User.get_user(username)
        if assignment and user:
            rel = Relationship(assignment, 'ASSIGNED_TO', user, relationship_id=self.relationship_id, assigned_date=date_assigned)
            graph.create(rel)
            return rel
        else:
            return None


    def create_assignment_course_rel(self, coursename, assignment_name, date_posted):
        assignment = Assignment.get_assignment_by_name(assignment_name)
        course = Course.get_course_by_name(coursename)
        if assignment and course:
            rel = Relationship(assignment, 'POSTED_TO', course, relationship_id=self.relationship_id, posted_date=date_posted)
            graph.create(rel)
            return rel
        else:
            return None

