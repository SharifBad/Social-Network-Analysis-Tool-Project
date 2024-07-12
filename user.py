
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            friend.friends.append(self)

    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            friend.friends.remove(self)

    def __repr__(self):
        return f"User({self.user_id}, {self.name})"
