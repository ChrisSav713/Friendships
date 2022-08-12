from contextlib import nullcontext
from flask_app.config.mysqlconnection import connectToMySQL

class Friendship:
    def __init__ (self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friendships" 
        results = connectToMySQL('friendships').query_db(query)
        favorites = []
        for favorites_item in results:
            favorites.append(cls(favorites_item))
        return favorites

    @classmethod
    def get_all_names(cls):
        query = '''
        SELECT CONCAT(users.first_name, ' ' , users.last_name) AS friend1, CONCAT(users2.first_name, ' ', users2.last_name) AS friend2
        FROM users
        JOIN friendships ON users.id = friendships.user_id
        JOIN users AS users2 ON friendships.friend_id = users2.id;
        '''
        return connectToMySQL('friendships').query_db(query)

    @classmethod
    def save(cls, data):
        query = '''
        INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
        VALUES( %(user_id)s, %(friend_id)s, NOW(), NOW())
        '''
        return connectToMySQL("friendships").query_db(query,data)

    @classmethod
    def check_exists(cls, data):
        query = '''
            SELECT *
            FROM friendships
            WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s;
            '''
        result = connectToMySQL('friendships').query_db(query,data)
        if len(result):
            return False 
        else:
            return True

