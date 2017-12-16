from py2neo import authenticate, Graph, Node, Relationship
import uuid

authenticate('localhost:7474', 'neo4j', 'A1b2c3d4')
graph = Graph('http://localhost:7474/db/data/')

class Grade:
    """
    initializes a username for an object of the Student class
    """
    def __init__(self, letter_grade, points, total_points, comment):
        self.grade_id = str(uuid.uuid4())
        self.letter_grade = letter_grade
        self.points = points
        self.total_points = total_points
        self.comment = comment

    def find(self):
        grade = graph.find_one('Grade', 'grade_id', self.grade_id)
        return grade


    """
    Checks if a grade_id already exists in the database and if not then Student is created with given username and password
    """
    def create_grade(self):
        if not self.find():
            grade = Node('Grade', grade_id=self.grade_id, letter_grade=self.letter_grade,
                           points=self.points, total_points=self.total_points, comment=self.comment)
            graph.create(grade)
            return True
        else:
            return False

    """
    Deletes student
    """
    def delete_grade(self):
        if self.find():
            graph.delete(self)
            return True
        else:
            return False

    def update_grade(self):
        if self.find():
            graph.push(self.find())
            return True
        else:
            return False