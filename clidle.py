

import random

from termcolor import colored

class Game:
    def __init__(self, word_list, tries=6):
        self.word_list = word_list
        self.tries = tries
        self.tries_left = tries
        self.inputs = []
        self.word = self._pick_word()

    def print_board(self):
        for i in range(self.tries):
            if self._has_input(i):
                guess = self.inputs[i]
                line = ""
                j = 0
                for c in guess:
                    if c == self.word[j]:
                        print(colored(c, 'green') + ' ', end='')
                    elif c in self.word:
                        print(colored(c, 'yellow') + ' ', end='')
                    else:
                        print(colored(c, 'red') + ' ', end='')
                    j += 1
                print()
            else:
                print('_ _ _ _ _')

    def guess(self, user_input):
        self.inputs.append(user_input)
        self.tries_left -= 1
        self.last_guess = user_input

    def is_won(self):
        return self.last_guess == self.word

    def is_lost(self):
        return self.tries_left == 0

    def _has_input(self, index):
        return len(self.inputs) >= index + 1

    def _pick_word(self):
        index = random.randint(0, len(self.word_list)-1)
        return self.word_list[index]


def _get_input(word_list):
    while True:
        user_input = input("Nova tentativa: ").upper()
        if user_input in word_list:
            return user_input
        else:
            print('\rPalavra inválida')


filename = 'pt-BR.dic'
word_list = open(filename).read().split('\n')
word_list = [string.upper() for string in word_list]

game = Game(word_list)
game.print_board()
while True:
    user_input = _get_input(word_list)
    game.guess(user_input)
    game.print_board()
    if game.is_won():
        print('GANHOU!')
        break
    elif game.is_lost():
        print('PERDEU!')
        print(f'A palavra era: {game.word}')
        break
