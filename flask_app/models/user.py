from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friends = []

    @classmethod
    def get_one(cls,data):
        query = '''
        SELECT * from users WHERE id = %{id}s;
        '''
        result = connectToMySQL('friendships').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = 'SELECT * from users;'
        results = connectToMySQL('friendships').query_db(query)
        users = []
        for user_item in results:
            users.append(cls(user_item))
        return users

    @classmethod
    def save(cls,data):
        query = '''
        INSERT INTO users (first_name, last_name, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, NOW(), NOW())
        '''
        return connectToMySQL('friendships').query_db(query,data)