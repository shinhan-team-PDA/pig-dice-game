from random import randint

# class computer
class Player:
    def __init__(self):
        self.score = 0
        self.bank = 0

    def bank(self):
        self.score += self.bank
        return self.score


class Computer(Player):
    def __init__(self):
        Player.__init__(self)


# class user
class User(Player):
    def __init__(self):
        Player.__init__(self)

# 사용자 정보 받기


# Roll 기능 구현

# Bank 기능 구현

# Roll stop
