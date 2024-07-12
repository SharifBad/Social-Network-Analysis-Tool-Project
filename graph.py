
from user import User

class Graph:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        if user_id not in self.users:
            user = User(user_id, name)
            self.users[user_id] = user
            return user
        else:
            print(f"User with ID {user_id} already exists.")
            return None

    def remove_user(self, user_id):
        if user_id in self.users:
            user = self.users.pop(user_id)
            for friend in user.friends:
                friend.friends.remove(user)
        else:
            print(f"User with ID {user_id} does not exist.")

    def get_user(self, user_id):
        return self.users.get(user_id, None)
