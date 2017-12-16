from py2neo import authenticate, Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import uuid

authenticate('localhost:7474', 'neo4j', 'A1b2c3d4')
graph = Graph('http://localhost:7474/db/data/')

class Message:
    """
    initializes a username for an object of the Message class
    """
    def __init__(self, title, text):
        self.message_id = str(uuid.uuid4())
        self.date_due = title
        self.points = text

    @staticmethod
    def get_message_by_id(message_id):
        return graph.find_one('Message', 'message_id', message_id)

    """
    Finds message based on message_id
    """
    def find(self):
        message = graph.find_one('Message', 'message_id', self.message_id)
        return message


    """
    Checks if a message_id already exists in the database and if not then message is created with given info
    """
    def create_message(self):
        if not self.find():
            message = Node('Message', message_id=self.message_id, title=self.title, text=self.text)
            graph.create(message)
            return True
        else:
            return False

    """
    Deletes message
    """
    def delete_message(self):
        if self.find():
            graph.delete(self)
            return True
        else:
            return False


    """
    Update message
    """
    def update_message(self):
        if self.find():
            graph.push(self.find())
            return True
        else:
            return False