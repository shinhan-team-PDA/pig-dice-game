from random import randint


# class computer
class Player:
    def __init__(self):
        self.total_score = 0
        self.tmp_score = 0

    def bank(self):
        self.total_score += self.tmp_score
        return self.tmp_score


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
def roll_dice() -> int:
    dice_num = randint(1,6+1)
    return dice_num


# Bank 기능 구현

# Roll stop
def should_stop(dice: int) -> bool:
    if dice == 1:
        return False
    else:
        return True







=======
>>>>>>> 012d6c7d7060b3f1cfe592c1ff28f8e635c1d1fa
