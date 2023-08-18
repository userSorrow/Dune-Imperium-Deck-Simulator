from src.player import Player

num_players = int(input("How many players?: "))
players = []
print()

# Player Creation
for i in range(0, num_players):
    print('NOTE: IF YOU WANT TO PLAY PAUL ATREIDES, TYPE "Paul"')
    current_leader = input("Player " + str(i + 1) + " - type your leader name: ")
    player = Player(current_leader)
    """ ADD CUSTOM STARTING HANDS LATER
    # Custom Starting Hand
    custom_hand = input("Custom starting hand? (y/n)").lower()
    if (custom_hand == "y" or custom_hand == "yes"):
        continue_add = True
        while continue_add:
            
    else:
        player.draw(5)
    """
    player.draw(5)

    players.append(player)
    print()

def prompt_command() -> str:
    response = input("Type a player command: ")
    while len(response) == 0:
        response = input("Type a player command: ")

    return response

playing = True
player_turn = 0
while playing:
    player = players[player_turn]
    print("Player " + str(player_turn + 1))

    # Prompt
    player_continues = True
    while player_continues:
        print(player)
        command_full = prompt_command().split()
        command = command_full[0].lower()
        command_full.pop(0)
        target_card = " ".join(command_full) or ""
        # unable to do match/case in vscode
        if command == "draw":
            if len(command_full) == 0:
                # Only 1 Card
                drawn = player.draw()[0]
                print("Drawn Card: " + drawn)
            else:
                num_draws = int(command_full[0]) # popped first element
                drawn = player.draw(num_draws)
                print("Drawn Cards: " + ", ".join(drawn))
        elif command == "discard":
            player.discardCard(target_card)
        elif command == "trash":
            player.trash(target_card)
        elif command == "acquire":
            player.acquire(target_card)
        elif command == "place":
            player.place_from_discard_to_top(target_card)
        elif command == "obtain":
            player.obtain_resources(target_card)
        elif command == "pass":
            player_continues = False
        print()

    print("\n\n\n")
    # Update player_turn
    player_turn = (player_turn + 1) % num_players

