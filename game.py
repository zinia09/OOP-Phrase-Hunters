from phrase import Phrase
import random

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.active_phrase = None
        self.guesses = [" "]

    def create_phrases(self):
        phrases = []
        phrases.append(Phrase("hello world"))
        phrases.append(Phrase("good morning"))
        phrases.append(Phrase("how are you"))
        phrases.append(Phrase("nice to meet you"))
        phrases.append(Phrase("Have a good day"))
        return phrases


    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        return random_phrase

#
#     def welcome(self):
#         print("============================\n  Welcome to Phrase Hunter\n============================")
#         print(f"“Number missed: {self.missed}")
#         display(active_phrase)
#

#
#
#     def get_guess():
#         get_guess = input(Enter a letter:)
#         return get_guess
#
#     def start():
#         append
#         check_guess(active_phrase)
#         if self.active_phrase.check_guess(user_guess):
#             print("YAY")
#         else:
#             print("Bummer!")

