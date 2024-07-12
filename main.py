
from graph import Graph

def main():
    # Create a new social network graph
    social_network = Graph()

    # Add users
    user1 = social_network.add_user(1, "Alice")
    user2 = social_network.add_user(2, "Bob")
    user3 = social_network.add_user(3, "Charlie")
    user4 = social_network.add_user(4, "David")
    user5 = social_network.add_user(5, "Eve")

    # Add friendships
    if user1 and user2:
        user1.add_friend(user2)
    if user2 and user3:
        user2.add_friend(user3)
    if user3 and user4:
        user3.add_friend(user4)
    if user4 and user5:
        user4.add_friend(user5)

    # Display users and their friends
    for user_id, user in social_network.users.items():
        print(f"{user.name}'s friends: {[friend.name for friend in user.friends]}")

    # Test BFS and DFS
    print("BFS from Alice:", social_network.bfs(1))
    print("DFS from Alice:", social_network.dfs(1))

    # Remove a user
    social_network.remove_user(2)

    # Display users and their friends after removal
    for user_id, user in social_network.users.items():
        print(f"{user.name}'s friends: {[friend.name for friend in user.friends]}")

    # Test BFS and DFS after removal
    print("BFS from Alice after removal:", social_network.bfs(1))
    print("DFS from Alice after removal:", social_network.dfs(1))

if __name__ == "__main__":
    main()
