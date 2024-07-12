
from graph import Graph

def main():
    # Create a new social network graph
    social_network = Graph()

    # Add users
    user1 = social_network.add_user(1, "Alice")
    user2 = social_network.add_user(2, "Bob")
    user3 = social_network.add_user(3, "Charlie")

    # Add friendships
    if user1 and user2:
        user1.add_friend(user2)
    if user2 and user3:
        user2.add_friend(user3)

    # Display users and their friends
    for user_id, user in social_network.users.items():
        print(f"{user.name}'s friends: {[friend.name for friend in user.friends]}")

    # Remove a user
    social_network.remove_user(2)

    # Display users and their friends after removal
    for user_id, user in social_network.users.items():
        print(f"{user.name}'s friends: {[friend.name for friend in user.friends]}")

if __name__ == "__main__":
    main()
