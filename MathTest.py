import random
import pygame as pg
import pygame.event
pg.init()

bg_color = (0, 0, 0)
size = width, height = 800, 800


donuts = 0
q = False
isnum = False
isnum2 = False
answer = -1
response = "null"
noun = "null"
sentence = "null"
space = " "
verb = "null"
verb2 = "null"
rand5 = -1
first_name = "null"
last_name = "null"
group = "null"
question = "null"
answer = 0
num1 = -1
num2 = -1

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
first_names = ["Joe", "Jeff", "Bob", "Harry", "John", "Jane", "Anna", "Caroline", "Olivia", "JimBob","Ava", "William", "Liam",
"Robert", "Arthur", "JJ", "Josh", "Eric", "Erica", "Curtis", "Danny", "Drew", "Bryan", "Matthew", "Emma", "Charlotte", "Sophia"]

last_names = ["Johnson", "Andrews", "Brown", "Davis", "Williams", "Miller", "Garcia", "Smith", "Gonzales", "Wilson", "Thomas",
"Taylor", "Moore", "Jackson", "Lee", "Young", "Walker", "Allen", "Adams", "Baker", "Campbell", "Evans", "Carter", "Cruz", "Bellagamba"]

verbs = ["bought", "stole", "inherited", "was given", "came across"]
verbs2 = ["buy", "steal", "inherit", "receive", "come across"]

groups = ["groups", "crates", "boxes", "containers", "bags"]

nouns = ["apples", "oranges", "bananas", "phones", "eggs", "water bottles", "blankets", "pillows", "plates"]

screen = pg.display.set_mode(size)
screen.fill(bg_color)
pg.display.flip()

def change_num(num):
   if num == "0":
       num = 0
   elif num == "1":
       num = 1
   elif num == "2":
       num = 2
   elif num == "3":
       num = 3
   elif num == "4":
       num = 4
   elif num == "5":
       num = 5
   elif num == "6":
       num = 6
   elif num == "7":
       num = 7
   elif num == "8":
       num = 8
   elif num == "9":
       num = 9
   elif num == "10":
       num = 10
   elif num == "11":
       num = 11
   elif num == "12":
       num = 12
   return num
def make_sentence():
   global donuts
   global answer
   global q
   group = groups[random.randint(0, 4)]
   first_name = first_names[random.randint(0, 26)]
   last_name = last_names[random.randint(0, 24)]
   full_name = first_name + " " + last_name
   rand5 = random.randint(0, 4)
   verb = verbs[rand5]
   verb2 = verbs2[rand5]
   num1 = nums[random.randint(2, 5)]
   num2 = nums[random.randint(2, 10)]
   noun = nouns[random.randint(0, 8)]
   answer = change_num(num1) * change_num(num2)
   sentence = full_name + space + verb + space + num1 + space + group + " each containing " + num2 + space + noun
   print(sentence)

   q = True
   while q:
       response = input("How many " + noun + " did " + full_name + space + verb2 + "?\n")
       isnum = response.isnumeric()
       if isnum:
           if response == str(answer):
               print("Correct!")
               donuts += answer/10
               q = False
           elif not response == str(answer):
               print("Try again")
       elif not isnum:
           print("That isn't a valid response")
while True:
   make_sentence()

