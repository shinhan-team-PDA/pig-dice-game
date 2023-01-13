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
    def __init__(self, name):
        Player.__init__(self)
        self.user_name = name


# 사용자 정보 받기
def input_user():
    print("============================")
    print("welcome to pig dice game!")
    user_name = input("Please Enter Your NAME: ")
    return User(user_name), Computer()

# Roll 기능 구현

# Bank 기능 구현

# Roll stop
