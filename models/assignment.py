from py2neo import authenticate, Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import uuid

authenticate('localhost:7474', 'neo4j', 'A1b2c3d4')
graph = Graph('http://localhost:7474/db/data/')

class Assignment:
    """
    initializes a username for an object of the Assignment class
    """
    def __init__(self, assignment_name, date_due, points, description):
        self.assignment_id = str(uuid.uuid4())
        self.assignment_name = assignment_name
        self.date_due = date_due
        self.points = points
        self.description = description

    @staticmethod
    def get_assignment_by_name(assignment_name):
        return graph.find_one('Assignment', 'assignment_name', assignment_name)

    """
    Finds assignment based on assignment_id
    """
    def find(self):
        assignment = graph.find_one('Assignment', 'assignment_id', self.assignment_id)
        return assignment


    """
    Checks if a assignment_id already exists in the database and if not then Assignment is created with given info
    """
    def create_assignment(self):
        if not self.find():
            assignment = Node('Assignment', assignment_id=self.assignment_id, date_due=self.date_due, points=self.points,
                           description=self.description, assignment_name=self.assignment_name)
            graph.create(assignment)
            return True
        else:
            return False

    """
    Deletes assignment
    """
    def delete_assignment(self):
        if self.find():
            graph.delete(self)
            return True
        else:
            return False


    """
    Update assignment
    """
    def update_assignment(self):
        if self.find():
            graph.push(self.find())
            return True
        else:
            return False