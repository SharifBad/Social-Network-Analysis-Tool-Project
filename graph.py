# graph.py

from user import User
from collections import deque

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

    def bfs(self, start_user_id):
        if start_user_id not in self.users:
            print(f"User with ID {start_user_id} does not exist.")
            return []

        visited = set()
        queue = deque([self.users[start_user_id]])
        result = []

        while queue:
            current_user = queue.popleft()
            if current_user.user_id not in visited:
                visited.add(current_user.user_id)
                result.append(current_user.user_id)
                for friend in current_user.friends:
                    if friend.user_id not in visited:
                        queue.append(friend)

        return result

    def dfs(self, start_user_id):
        if start_user_id not in self.users:
            print(f"User with ID {start_user_id} does not exist.")
            return []

        visited = set()
        stack = [self.users[start_user_id]]
        result = []

        while stack:
            current_user = stack.pop()
            if current_user.user_id not in visited:
                visited.add(current_user.user_id)
                result.append(current_user.user_id)
                for friend in current_user.friends:
                    if friend.user_id not in visited:
                        stack.append(friend)

        return result
