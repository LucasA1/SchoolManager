from py2neo import authenticate, Graph, Node
import uuid

authenticate('localhost:7474', 'neo4j', 'A1b2c3d4')
graph = Graph('http://localhost:7474/db/data/')


class Course:
    """
    initializes a username for an object of the Course class
    """

    def __init__(self, course_name, credits, description):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.credits = credits
        self.description = description

    @staticmethod
    def get_course_by_id(course_id):
        course = graph.find_one('Course', 'course_id', course_id)
        return course

    @staticmethod
    def get_course_by_name(course_name):
        course = graph.find_one('Course', 'course_name', course_name)
        return course

    """
    Finds course based on course_id
    """
    def find(self):
        course = graph.find_one('Course', 'course_name', self.course_name)
        return course

    """
    Checks if a course_id already exists in the database and if not then Course is created with given info
    """

    def create_course(self):
        if not self.find():
            course = Node('Course', course_id=self.course_id, course_name=self.course_name, credits=self.credits, description=self.description)
            graph.create(course)
            return True
        else:
            return False

    """
    Deletes course
    """

    def delete_course(self):
        if self.find():
            graph.delete(self)
            return True
        else:
            return False

    """
    Update course
    """

    def update_course(self):
        if self.find():
            graph.push(self.find())
            return True
        else:
            return False
