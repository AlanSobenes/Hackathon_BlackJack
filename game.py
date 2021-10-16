from classes.deck import Deck

class Player:
    player_deck = Deck()
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.status = True
        self.listofcards = []
        self.instant = False
    
    def checkCards(self):
        
        self.score += self.listofcards[len(self.listofcards)-1]
        
        if self.score > 21:
            print("Dealer won!")
            self.instant = True
            self.status = False
            
        if self.score == 21:
            print("You won!")
            self.instant = True
            self.status = False
    
    def stay(self):
        self.status = False

    def hit(self):
        self.listofcards.append(self.player_deck.hit())
        self.checkCards()
        return self

    def deal(self):
        self.hit().hit()
        self.printScore()

    def printScore(self):
        print(f"{self.name} has a score of {self.score}")
        return self

class Dealer(Player):
    def __init__(self): 
        super().__init__(self)
        self.score = 0
        self.status = True
        self.listofcards = []
        self.instant = False
    
    def checkCards(self):
        super().checkCards()
    
    def hit(self):
        super().hit()
    
    def deal(self):
        super().hit().hit()
        print(f"Dealer's First Card: {self.listofcards[0]}")

player1 = Player("Player1")
player2 = Dealer()
player1.deal()
player2.deal()

while player1.status == True and player2.status == True:
    answer = input('Hit or Stay?\n')
    answer = answer.lower()
    if answer == "hit":
        player1.hit()
    else:
        player1.stay()
        while player2.score <= 13:
            player2.hit()
        if player1.score > player2.score:
            print ("You won!")
        else:
            print ("Dealer won!")
    player1.printScore()

        