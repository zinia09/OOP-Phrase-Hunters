from game import Game

# from phrase import Phrase

# phrase = Phrase()
# game = Game()

# print(phrase)
# print(game)

# phrase = Phrase("Life is Mike a box of chocolates")
# print(phrase.phrase)
#
game = Game()
for phrase in game.create_phrases():
    print(phrase.phrase)

def print_phrase(phrase_object):
    print(f"The phrase is: {phrase_object.phrase}")
game = Game()
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())
print_phrase(game.get_random_phrase())

# if __name__ == "__main__":
#     main()
#
# game = Game()
# game.welcome()
#
# # Inside Dunder Main:
# ## Create an instance of your Game class
# ## Start your game by calling the instance method that starts the game loop
#