import random

class Player:
    def __init__(self, leader) -> None:
        self.leader = leader
        self.deck = Player.make_starting_deck() # [last card, ... third card, second card, top card]
        self.discard = []
        self.hand = []
        self.resources = {"Spice": 0, 
                          "Solaris": 0, 
                          "Water": 0 }
        self.isPaul = False
        if (self.leader.split()[0].lower() == "paul"):
            self.isPaul = True

    def peek(self):
        if self.isPaul:
            return self.deck[len(self.deck) - 1]
        else:
            raise Exception("cannot peek top card without being Paul Atreides")
        
    def draw(self, num = 1):
        drawn = []
        for i in range(0, num):
            if len(self.deck) == 0 and len(self.discard) == 0:
                print("DID NOT DRAW, NO MORE CARDS IN DECK OR DISCARD") # SHOULD BE EXCEPTION INSTEAD
            elif len(self.deck) == 0:
                self.shuffle_discard_into_deck()
            else:
                card = self.deck.pop()
                drawn.append(card)
                self.hand.append(card)
        if len(drawn) == 0:
            return ["NONE"]
        return drawn
    
    def discardCard(self, card_name):
        for i in range(0, len(self.hand)):
            current_card = self.hand[i]
            if (current_card.lower() == card_name.lower()):
                self.discard.append(current_card)
                self.hand.pop(i)
                return True
        
        print("DID NOT DISCARD CARD") # SHOULD THROW EXCEPTION
        return False
    
    def trash(self, card_name):
        if card_name.lower() in (card.lower() for card in self.discard):
            self.discard.remove(card_name)
        elif card_name.lower() in (card.lower() for card in self.hand):
            self.hand.remove(card_name)
        else:
            print("DID NOT TRASH CARD") # SHOULD THROW EXCEPTION
    
    def shuffle_discard_into_deck(self):
        random.shuffle(self.discard)
        while len(self.discard) > 0:
            self.deck.append(self.discard.pop())

    def place_from_discard_to_top(self, target_card):
        for i in range(0, len(self.discard)):
            current = self.discard[i]
            if current == target_card:
                self.deck.append(current)
                self.discard.pop(i)
                return current
            
    def acquire(self, card_name):
        self.discard.append(card_name)
        
    def obtain_resources(self, resource_type):
        if resource_type.capitalize() not in self.resources.keys():
            print("Wrong type of resource") # you can put an exception error here
        else:
            amt = int(input("How much? "))
            self.resources[resource_type.capitalize()] += amt  
            
        
    def make_starting_deck():
        starting_deck = ["Signet Ring", "Seek Allies", "Diplomacy", "Dagger", "Dagger", "Reconnaissance", "Dune, The Desert Planet", "Dune, The Desert Planet", "Convincing Argument", "Convincing Argument"]
        random.shuffle(starting_deck)
        return starting_deck
    
    def __str__(self) -> str:
        peek_str = ""
        if (self.isPaul and len(self.deck) > 0):
            peek_str = ", Top Card: " + self.peek()
        return f"""{self.leader}
deck: {len(self.deck)} count{peek_str}
discard: {self.discard}
hand: {self.hand}
resources: {[key + " : " + str(value) for key, value in self.resources.items()]}
        """