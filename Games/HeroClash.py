import time

print("*************** WELCOME TO THE BATTLE GAME ****************")

# Character information
characters = {
    "batman": {"life": 100, "hit": {"punch": 25, "kick": 30, "slap": 20}},
    "ironman": {"life": 120, "hit": {"punch": 20, "kick": 35, "slap": 15}},
    "hulk": {"life": 200, "hit": {"punch": 50, "kick": 40, "slap": 30}},
    "spiderman": {"life": 80, "hit": {"punch": 30, "kick": 25, "slap": 10}}
}

try:
    # Display available characters
    print("\nAvailable Characters:")
    for name, stats in characters.items():
        print(f"{name.capitalize()} - Life: {stats['life']}")

    # Get valid character choices from users
    while True:
        user1 = input("\nUser 1, choose your character: ").lower()
        if user1 in characters:
            break
        print("Invalid choice! Please select from the list.")

    while True:
        user2 = input("User 2, choose your character: ").lower()
        if user2 in characters and user2 != user1:
            break
        print("Invalid choice! Please select a different character.")

    # Store chosen character stats
    user1_stats = characters[user1].copy()
    user2_stats = characters[user2].copy()

    print(f"\n{user1.capitalize()} vs {user2.capitalize()} - LET THE BATTLE BEGIN!\n")
    time.sleep(1.5)

    # Battle starts
    while user1_stats["life"] > 0 and user2_stats["life"] > 0:
        # User 1 attacks
        attack = input(f"\n{user1.capitalize()}, choose your attack (punch/kick/slap): ").lower()
        if attack in user1_stats["hit"]:
            damage = user1_stats["hit"][attack]
            user2_stats["life"] -= damage
            print(f"{user1.capitalize()} used {attack}! {user2.capitalize()} lost {damage} life points.")
        else:
            print("Invalid attack! You missed your turn.")

        if user2_stats["life"] <= 0:
            print(f"\n{user2.capitalize()} has fallen! {user1.capitalize()} WINS! 🏆")
            break

        time.sleep(1)

        # User 2 attacks
        attack = input(f"\n{user2.capitalize()}, choose your attack (punch/kick/slap): ").lower()
        if attack in user2_stats["hit"]:
            damage = user2_stats["hit"][attack]
            user1_stats["life"] -= damage
            print(f"{user2.capitalize()} used {attack}! {user1.capitalize()} lost {damage} life points.")
        else:
            print("Invalid attack! You missed your turn.")

        if user1_stats["life"] <= 0:
            print(f"\n{user1.capitalize()} has fallen! {user2.capitalize()} WINS! 🏆")
            break

        time.sleep(1)

except KeyboardInterrupt:
    print("\n\nGame interrupted! Exiting safely...")

except Exception as e:
    print(f"\nAn error occurred: {e}")
