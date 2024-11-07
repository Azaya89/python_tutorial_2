# Controls flows are ways to direct the flow of your code logic.
# some syntax include: 'if', 'elif', 'else', 'or', 'and', 'for', 'while', 'try', 'except'

# while True:
#     score = int(input("What did you score?: "))
#     prompt = input("Do you want to continue?(y/n): ")
#     if not prompt == 'y':
#         break

# range -  a way to generate a sequence of integers of any length

evens = list(range(2, 11, 2))
odds = list(range(1,11, 2))
# print(evens)
# print(odds)

div_five = list(range(100, 0, -5))
# print(div_five)

message = "I will never steal again!"

# for _ in range(5):
#     print(message)

num = 0
# while num < 5: # this loop runs as long as 'num' is less than 5. It terminates when 'num' >= 5
#     print(message)
#     num += 1

names = ['obi', 'ada', 'mike', 'chike', 'ayo']

# for name in names:
#     if name == 'obi':
#         print(f"Welcome to the show Mr {name.title()}")
#     else:
#         print(f"You are not Mr Obi. Your name is {name.title()}")

