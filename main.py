import sys
import random
from itertools import chain

class testing(object):
    def __init__(self, filename):
        self.filename = filename
        self.words = self.file_to_text()
    def file_to_text(self):
        with open(self.filename, "r") as file_opened:
            print(list(chain.from_iterable(line.split() for line in file_opened)))



def main():

	trivia = testing("alice.txt").file_to_text()


