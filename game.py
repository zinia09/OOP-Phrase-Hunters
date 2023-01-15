from phrase import Phrase
import random


class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = []
        self.guesses = [" "]
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()

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

    def welcome(self):
        print("============================\n  Welcome to Phrase Hunter\n============================")

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"\nNumber missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()

    def get_guess(self):
        return input("\nEnter a letter: ")

    def game_over(self):
        if self.missed >= 5:
            print("Sorry you lost")
        else:
            print("Congratulations! You Won!")
