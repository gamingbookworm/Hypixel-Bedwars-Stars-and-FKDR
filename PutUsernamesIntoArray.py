#use command prompt to run
#cd documents
#cd bedwars stats project
#python PutUsernamesIntoArray.py

usernames = []

# get 50 player names
for i in range(50):
    name = input("Enter player name: ")
    usernames.append(name)

# print the usernames array in the format ["player1", "player2", ..., "player50"]
formatted_usernames = ', '.join(f'"{name}"' for name in usernames)
print(f"usernames = [{formatted_usernames}]")