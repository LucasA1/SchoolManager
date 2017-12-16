from py2neo import authenticate, Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import uuid

authenticate('localhost:7474', 'neo4j', 'A1b2c3d4')
graph = Graph('http://localhost:7474/db/data/')


class User:
    """
    initializes a username for an object of the User class
    """
    def __init__(self, username, user_id, user_type, firstname, lastname, email):
        self.username = username
        self.user_id = user_id
        self.user_type = user_type
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    @staticmethod
    def get_user(username):
        return graph.find_one('User', 'username', username)

    @staticmethod
    def delete_user(username):
        user = get_user(username)
        if user:
            graph.delete(user)

    @staticmethod
    def verify_exists(username, password):
        user = User.get_user(username)
        if user:
            return bcrypt.verify(password, user['password'])
        else:
            return False


    """
    finds a node in the database labeled :User with the given username
    returns a py2neo.Node object
    """
    def find(self):
        user = graph.find_one('User', 'username', self.username)
        return user

    """
    Checks if a username already exists in the database and if not then User is created with given username and password
    """
    def register(self, password):
        if not self.find():
            user = Node('User',
                        username=self.username,
                        password=bcrypt.encrypt(password),
                        user_id=self.user_id,
                        user_type = self.user_type,
                        firstname=self.firstname,
                        lastname=self.lastname,
                        email=self.email)
            graph.create(user)
            return True
        else:
            return False


    "Verifies the input password"
    def verify_password(self, password):
        user = self.find()
        if user:
            return bcrypt.verify(password, user['password'])
        else:
            return False
    """
    Finds user in the database
    creates a post node and generates random id with uuid4() and adds date and timestamp using created functions date() and timestamp()
    creates a relationship between user and post nodes called PUBLISHED.
    Tags are split by commas and lowercased and a tag TAGGED post relationship is created for each tag.
    """
    def add_post(self, title, text):
        user = self.find()
        post = Node(
            'Post',
            id=str(uuid.uuid4()),
            title=title,
            text=text,
            timestamp=timestamp(),
            date=date()
            )
        rel = Relationship(user, 'PUBLISHED', post)
        graph.create(rel)

        # tags = [x.strip() for x in tags.lower().split(',')]
        # for name in set(tags):
        #     tag = Node('Tag', name=name)
        #     graph.merge(tag)
        #
        #     rel = Relationship(tag, 'TAGGED', post)
        #     graph.create(rel)


def get_todays_recent_posts():
    query = '''
    MATCH (user:User)-[:PUBLISHED]->(post:Post)
    WHERE post.date = {today}
    RETURN user.username AS username, post
    ORDER BY post.timestamp DESC LIMIT 5
    '''

    return graph.run(query, today=date())


def timestamp():
    epoch = datetime.utcfromtimestamp(0)
    now = datetime.now()
    delta = now - epoch
    return delta.total_seconds()


def date():
   return datetime.now().strftime('%Y-%m-%d')
