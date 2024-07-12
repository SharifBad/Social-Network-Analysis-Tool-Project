class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = {}  # Dictionary to store friends with weights

    def add_friend(self, friend, weight=1):
        if friend not in self.friends:
            self.friends[friend] = weight
            friend.friends[self] = weight

    def remove_friend(self, friend):
        if friend in self.friends:
            del self.friends[friend]
            del friend.friends[self]

    def __repr__(self):
        return f"User({self.user_id}, {self.name})"
