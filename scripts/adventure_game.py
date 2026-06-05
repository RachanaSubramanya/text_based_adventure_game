# adventure_game.py

# You are an explorer who is searching for a mysterious treasure hidden deep within a jungle.

def game_intro():
    print("Welcome to the Jungle Adventure!")
    print("You are an explorer searching for a mysterious treasure hidden deep within the jungle.")
    print("Your journey will be filled with challenges and dangers, but the reward is worth it.")
    print("Good luck on your adventure!")

def choose_path():
    print("\nYou come to a fork in the path. Do you go left towards the river or right towards the mountain?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == 'left':
        river_path()
    elif choice == 'right':        
        mountain_path()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        choose_path()

def river_path():
    print("\nYou follow the path towards the river. As you walk, you hear the sound of rushing water.")
    print("You come across a rickety bridge that looks like it might collapse if you cross it.")
    choice = input("Do you want to cross the bridge? Type 'yes' or 'no': ").lower()
    if choice == 'yes':
        print("\nYou carefully cross the bridge, but halfway across it starts to wobble!")
        print("You manage to make it to the other side safely, but the bridge collapses behind you.")
        print("You continue on your journey and eventually find the treasure hidden in a cave by the river.")
        print("Congratulations! You found the treasure!")
    elif choice == 'no':
        print("\nYou decide not to risk crossing the bridge and turn back.")
        choose_path()  
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        river_path() 

def mountain_path():
    print("\nYou follow the path towards the mountain. The climb is steep and treacherous.")
    print("As you ascend, you encounter a group of wild animals blocking your path.")
    choice = input("Do you try to scare them away or find another route? Type 'scare' or 'find': ").lower()
    if choice == 'scare':
        print("\nYou try to scare the animals away, but they become aggressive and attack you.")
        print("You manage to escape, but you are injured and have to turn back.")
        choose_path()  
    elif choice == 'find':
        print("\nYou decide to find another route around the animals. After a long detour, you successfully bypass them.")
        print("The climb continues to be difficult, and the path becomes more dangerous, but you persevere and eventually reach the summit.")
        print("At the summit, the sky is beautiful, with the sunset casting a warm glow over the landscape.")
        print("You feel a sense of accomplishment and wonder at the breathtaking view.")
        print("A you stand enjoying the view, a sudden gust of wind blows, and you lose your footing, falling down the mountain.")
        print("You wake up in a hospital bed, realizing that you survived the fall but are badly injured.")
        print("You have to give up your quest for the treasure and focus on recovering from your injuries.")
        print("Although you didn't find the treasure, you are grateful to be alive and have learned valuable lessons from your adventure.")
        print("You fought well, and your bravery and determination will be remembered.")
    else:
        print("Invalid choice. Please choose 'scare' or 'find'.")
        mountain_path()

def main():
    game_intro()
    choose_path()

if __name__ == "__main__":
    main()