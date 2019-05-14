#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.myEnemyLastMove = self.myLastMove = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.myLastMove = my_move
        self.myEnemyLastMove = their_move


class RandomPlayer (Player):
    def move(self):
        randomMove = random.choice(moves)
        return randomMove


class HumanPlayer (Player):
    def move(self):
        humanMove = input("what your move is going to be: ").lower()
        while humanMove not in moves:
            print("please type in one of the universal moves: rock, paper, scissors")
            humanMove = input("what your move is going to be: ").lower()
        return humanMove


class ReflectPlayer(Player):
    def move(self):
        return self.myEnemyLastMove


class CyclePlayer (Player):
    def move(self):
        moveIndex = moves.index(self.myLastMove)
        if moveIndex < 2:
            cycleMove = moves[moveIndex + 1]
        else:
            cycleMove = moves[0]

        return cycleMove


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        # to determine the winner each round and keep score
        if beats(move1, move2):
            self.p1.score += 1
            print("\nPlayer1 is the WINNER")
        elif beats(move2, move1):
            self.p2.score += 1
            print("\nPlayer2 is the WINNER")
        else:
            print("\nit is a tie")
        print(f"Player 1: {self.p1.score}  Player 2: {self.p2.score}")

        # to update the learn function every round
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\nGame start!")
        for round in range(3):
            print(f"\nRound {round}:")
            self.play_round()
        print("Game over!")

        # show the final winner of all rounds
        if self.p1.score == self.p2.score:
            print("IT IS A TIE")
        elif self.p1.score > self.p2.score:
            print("\nThe winner of all rounds is: Player1\n")
        else:
            print("\nThe winner of all rounds is: Player2\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
