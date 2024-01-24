#Regular Imports
import random

#Functions
def rand_card():
   var = cards[random.randint(0, 3)][random.randint(0, 12)]
   while var.used:
       var = cards[random.randint(0, 3)][random.randint(0, 12)]
   var.used = True
   return var
#Card Class
class Card:
   def __init__(self, number, icon):
       self.number = number
       self.icon = icon
       self.used = False
       self.in_flush = False
       self.in_straight = False
       self.score = 0
       try:
           match self.number:
               case "J":
                   self.score = 11
               case "Q":
                   self.score = 12
               case "K":
                   self.score = 13
               case "A":
                   self.score = 14
       except:
           self.score = int(self.number)


#Player Class
class player:
   global cards
   def __init__(self, player_num, balance):
       self.name = "player" + str(player_num)
       self.num = player_num
       self.type = 0
       self.is_out = False
       self.hole = []
       self.balance = balance
       self.has_folded = False
       self.amt_to_call = 0
       self.max_win = 0
       self.all_cards = []
       self.card_score = 0
       self.highscore = 0
       self.num_of_suits = [0,0,0,0] #hearts,clubs,diamonds,spades
       self.high_card_in_flush = 0
       self.high_card_in_straight = 0
   def get_score(self):
       global game
       self.all_cards.append(game.com_cards)
       self.all_cards.append(self.hole)
       #Royal Flush 117
       #Striaght Flush 104
       #Quad 91
       #Full House 78
       #Flush 65
       #Straight 52
       #Trio 39
       #Two Pair 26
       #Pair 13
       #High Card 0


       for x in self.all_cards:
           for y in self.all_cards:
               #Pair
               if x == y:
                   pass
               elif self.all_cards[x].score == self.all_cards[y].score:
                   if self.highscore < self.all_cards[x] + 13:
                       self.highscore = self.all_cards[x] + 13
                   for z in self.all_cards:
                       if x == z or y == z:
                           pass
                       elif self.all_cards[x].score == self.all_cards[z].score:
                           if self.highscore < self.all_cards[x] + 39:
                               self.highscore = self.all_cards[x] + 39
                       for a in self.all_cards:
                           if a == x or a == y or a == z:
                               pass
                           elif self.all_cards[z].score == self.all_cards[a].score:
                               #Two Pair
                               if self.highscore < self.all_cards[x] + 26 and self.all_cards[x].score > self.all_cards[z].score:
                                   self.highscore = self.all_cards[x] + 26
                               if self.highscore < self.all_cards[z] + 26 and self.all_cards[x].score < self.all_cards[z].score:
                                   self.highscore = self.all_cards[z] + 26
                               #Quad
                               if self.highscore < self.all_cards[x] + 91 and self.all_cards[x].score == self.all_cards[z].score:
                                   self.highscore = self.all_cards[x] + 91
                           for b in self.all_cards:
                               if x == b or y == b or z == b or a == b:
                                   pass
                               elif self.all_cards[x].score + 4 == self.all_cards[b].score:
                                   if self.all_cards[x].score + 3 == self.all_cards[a].score:
                                       if self.all_cards[x].score + 2 == self.all_cards[z].score:
                                           if self.all_cards[x].score + 1 == self.all_cards[y].score and self.highscore < self.all_cards[x].score + 52:
                                               self.highscore = self.all_cards[x].score + 52
                                               self.high_card_in_straight = self.all_cards[x].score


           #Flush
           match self.all_cards[x].icon:
               case "diamond":
                   self.num_of_suits[2] += 1
                   self.all_cards[x].in_flush = True
                   if self.high_card_in_flush.score < self.all_cards[x].score:
                       self.high_card_in_flush = self.all_cards[x].score
               case "heart":
                   self.num_of_suits[3] += 1
                   self.all_cards[x].in_flush = True
                   if self.high_card_in_flush.score < self.all_cards[x].score:
                       self.high_card_in_flush = self.all_cards[x].score
               case "spade":
                   self.num_of_suits[0] += 1
                   self.all_cards[x].in_flush = True
                   if self.high_card_in_flush.score < self.all_cards[x].score:
                       self.high_card_in_flush = self.all_cards[x].score
               case "club":
                   self.num_of_suits[1] += 1
                   self.all_cards[x].in_flush = True
                   if self.high_card_in_flush.score < self.all_cards[x].score:
                       self.high_card_in_flush = self.all_cards[x].score


       for x in self.num_of_suits:
           if self.num_of_suits[x] >= 5:
               if self.highscore <= self.high_card_in_flush.score + 65:
                   pass
               else:
                   #Stright/Royal Flush
                   self.highscore = self.high_card_in_flush.score + 65
                   if self.high_card_in_straight == self.high_card_in_flush:
                       self.highscore = self.high_card_in_straight
       for x in self.all_cards:
           if self.all_cards[x].score > self.highscore:
               self.highscore = self.all_cards[x].score


   #Player Actions
   def move(self):
       if not self.has_folded:
           if self.type == 0:
               while response != "":
                   response = input("What would you like to do?\nf = Fold\n b = Bet\nc = Call\nC = Check")
                   if response.isnumeric():
                       print("That isn't a valid response")
                   elif response == "f":
                       self.fold()
                   elif response == "b":
                       response = input("How much would you like to bet?")
                       if response.isnumeric():
                           self.bet(int(response))
                       else:
                           print("That isn't a valid response")
                   elif response == "c":
                       self.call()
                   elif response == "C":
                       self.check()
           elif self.type == 1:
               pass
   def fold(self):
       self.has_folded = True
       print(self.name + " has folded")
       game.players_playing -= 1
   def check(self):
       print(self.name + " has checked")
   def bet(self, amount):
       global game
       if self.balance <= amount:
           game.pot += self.balance
           self.balance = 0
           print(self.name + " has gone all in with a bet of $" + str(amount))
       else:
           game.pot += self.balance
           self.balance -= amount
           print(self.name + " has bet $" + str(amount))
   def call(self):
       print(self.name + " has called")
       if self.balance <= self.amt_to_call:
           self.balance = 0
           self.max_win = game.pot
   def eliminate(self):
       players[self.num].remove()
       print(self.name + " has been eliminated")
       game.players_left -= 1
       del self


#Game class
class game:
   def __init__(self, blinds, player_count):
       self.cycles = 0
       self.blinds = blinds
       self.pot = 0
       self.round_num = 0
       self.players_playing = player_count
       self.com_cards = []
       self.player_turn = 0
       self.players_left = player_count
       self.starting_player = 0
       self.cards_left = 5
   def cycle(self):
       global var1
       for x in range(0,3):
           for y in range(0,12):
               cards[x][y].used = False
       for x in range(0, self.players_left - 1):


           if players[x].balance <= 0:
               players[x].eliminate()
           players[x].all_cards = players[x].hole + self.com_cards
           players[x].hole = [rand_card(), rand_card()]
           players[x].has_folded = False
           players[x].amt_to_call = 0
           players[x].max_win = 0
           players[x].card_score = 0
           players[x].highscore = 0
           players[x].num_of_suits = [0, 0, 0, 0]  # hearts,clubs,diamonds,spades
           players[x].high_card_in_flush = 0
           players[x].high_card_in_straight = 0
       self.cards_left = 5
       self.com_cards = [rand_card(),rand_card(),rand_card(),rand_card(),rand_card()]
       self.players_playing = self.players_left
       var1 += 1
       self.next_deal(var1)
       if self.players_left == self.starting_player:
           self.starting_player = self.players_left
       else:
           self.starting_player += 1




       #Blinds
       self.round_num += 1
       match self.round_num:
           case 10:
               self.blinds = [20, 50]
           case 25:
               self.blinds = [30, 75]
           case 50:
               self.blinds = [50, 100]
           case 100:
               self.blinds = [75, 150]
           case 250:
               self.blinds = [150, 300]
           case 500:
               self.blinds = [250, 500]
   def next_player(self,player_num):
       if player_num == self.starting_player:
           self.next_deal()
       elif player_num <= self.players_left:
           players[player_num + 1].move()
       elif player_num > self.players_left:
           players[0].move()
   def next_deal(self,deal_num):
       match deal_num:
           case 1:
               for x in range(1,3):
                   self.com_cards.append(rand_card())
                   self.cards_left -= 1
               for x in range(0, self.players_left - 1):
                   if players[x].balance == 0:
                       players[x].max_win = self.pot
               self.next_player(players[self.starting_player])
           case 2:
               self.com_cards.append(rand_card())
               self.cards_left -= 1
               for x in range(0, self.players_left - 1):
                   if players[x].balance == 0:
                       players[x].max_win = self.pot
               self.next_player(players[self.starting_player])
           case 3:
               self.com_cards.append(rand_card())
               self.cards_left -= 1
               for x in range(0, self.players_left - 1):
                   if players[x].balance == 0:
                       players[x].max_win = self.pot
               self.next_player(players[self.starting_player])








#Vars
response = ""
var1 = 0
var = []
#Cards Setup
cards = []
cards.append([Card("2","heart"),Card("3","heart"),Card("4","heart"),Card("5","heart"),Card("6","heart"),Card("7","heart"),Card("8","heart"),Card("9","heart"),Card("10","heart"),Card("J","heart"),Card("Q","heart"),Card("K","heart"),Card("A","heart")])
cards.append([Card("2","diamond"),Card("3","diamond"),Card("4","diamond"),Card("5","diamond"),Card("6","diamond"),Card("7","diamond"),Card("8","diamond"),Card("9","diamond"),Card("10","diamond"),Card("J","diamond"),Card("Q","diamond"),Card("K","diamond"),Card("A","diamond")])
cards.append([Card("2","spade"),Card("3","spade"),Card("4","spade"),Card("5","spade"),Card("6","spade"),Card("7","spade"),Card("8","spade"),Card("9","spade"),Card("10","spade"),Card("J","spade"),Card("Q","spade"),Card("K","spade"),Card("A","spade")])
cards.append([Card("2","club"),Card("3","club"),Card("4","club"),Card("5","club"),Card("6","club"),Card("7","club"),Card("8","club"),Card("9","club"),Card("10","club"),Card("J","club"),Card("Q","club"),Card("K","club"),Card("A","club")])


#Players Setup
players = []
player_count = 8
for x in range(1, player_count):
   players.append(player(x, 1000))


#Game Setup
game([10, 20], player_count)




game.cycle(game([10, 20], player_count))


#TO-DO
#Blinds
#Finish amt to call
#Finish system for switching to a new round
#Linking things together
#Finish switching classes to caps
#Organize
#Debug

