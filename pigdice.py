from random import randint


# class computer
class Player:
    def __init__(self):
        self.total_score = 0
        self.tmp_score = 0

    def bank(self):
        self.total_score += self.tmp_score
        return self.tmp_score
    
    # Roll 기능 구현
    def roll_dice(self) -> int:
        dice_num = randint(1,6+1)
        if self.should_stop(dice_num) :
            self.bank()
        else:
            self.tmp_score += dice_num
        return dice_num
    
    # type(r,s) 판단
    def should_roll(self, type_):
        if type_ == 'r':
            self.roll_dice()
        else :
            self.bank()
    
    # Roll stop
    def should_stop(self,dice: int) -> bool:
        if dice == 1:
            return True
        else:
            return False

    def is_win(self):
        if self.total_score >= 50:
            return True
        else:
            return False


class Computer(Player):
    def __init__(self):
        Player.__init__(self)
        self.roll_num = randint(1, 10 + 1)

    def computer_roll(self):
        for _ in range(self.roll_num):
            dice = self.roll_dice()
            self.should_stop(dice)




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

