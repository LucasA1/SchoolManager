from py2neo import authenticate, Graph, Node
import uuid

authenticate('localhost:7474', 'neo4j', 'A1b2c3d4')
graph = Graph('http://localhost:7474/db/data/')

class Event:
    """
    initializes a username for an object of the Event class
    """
    def __init__(self, event_date, event_name, description):
        self.event_id = str(uuid.uuid4())
        self.event_date = event_date
        self.event_name = event_name
        self.description = description

    """
    Finds event based on event_id
    """
    def find(self):
        event = graph.find_one('Event', 'event_id', self.event_id)
        return event


    """
    Checks if a event_id already exists in the database and if not then Event is created with given info
    """
    def create_event(self):
        if not self.find():
            event = Node('Event', event_id=self.event_id, event_date=self.event_date, points=self.points,
                           description=self.description)
            graph.create(event)
            return True
        else:
            return False

    """
    Deletes event
    """
    def delete_event(self):
        if self.find():
            graph.delete(self)
            return True
        else:
            return False


    """
    Update event
    """
    def update_event(self):
        if self.find():
            graph.push(self.find())
            return True
        else:
            return False