from user import User
from collections import deque
import heapq

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
                del friend.friends[user]
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

    def dijkstra(self, start_user_id, target_user_id):
        if start_user_id not in self.users or target_user_id not in self.users:
            print("One or both users do not exist.")
            return []

        start_user = self.users[start_user_id]
        target_user = self.users[target_user_id]

        distances = {user: float('infinity') for user in self.users.values()}
        previous_users = {user: None for user in self.users.values()}
        distances[start_user] = 0
        priority_queue = [(0, start_user)]

        while priority_queue:
            current_distance, current_user = heapq.heappop(priority_queue)

            if current_distance > distances[current_user]:
                continue

            for neighbor, weight in current_user.friends.items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_users[neighbor] = current_user
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current_user = target_user
        while previous_users[current_user] is not None:
            path.append(current_user.user_id)
            current_user = previous_users[current_user]
        path.append(start_user.user_id)
        path.reverse()

        return path
