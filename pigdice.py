from random import randint


# class computer
class Player:
    def __init__(self, name):
        self.total_score = 0
        self.tmp_score = 0
        self.name = name

    def bank(self):
        self.total_score += self.tmp_score
        return self.tmp_score

    # Roll 기능 구현
    def roll_dice(self) -> int:
        print("주사위를 던집니다.")
        dice_num = randint(1, 6)
        print(f"주사위는 {dice_num}입니다.")
        if self.should_stop(dice_num):
            print(f"1이 나왔으므로, {self.name}의 차례는 끝났습니다.")
            print(f"{self.name}의 총점은 {self.total_score}점 입니다.")
        else:
            self.tmp_score += dice_num
            print(f"이번 차례의 획득 점수는 {self.tmp_score}점 입니다.")
        return dice_num

    # type(r,s) 판단

    # Roll stop
    def should_stop(self, dice: int) -> bool:
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
        Player.__init__(self, "computer")
        self.roll_num = randint(1, 10 + 1)

    def computer_roll(self):
        for _ in range(self.roll_num):
            dice = self.roll_dice()
            if self.should_stop(dice):
                self.tmp_score = 0
                break
        self.bank()


# class user
class User(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def should_roll(self, type_):
        if type_ == 'r':
            return True
        else:
            self.bank()
            print(f"{self.name}의 총점은 {self.total_score}점 입니다.")
            return False


# 사용자 정보 받기
def input_user():
    print("============================")
    print("welcome to pig dice game!")
    user_name = input("Please Enter Your NAME: ")
    return User(user_name), Computer()


def game():
    user, computer = input_user()
    win = False
    while not win:
        should_roll = True
        print("=========================")
        print("당신의 차례입니다.")
        print("=========================")
        while should_roll:
            dice = user.roll_dice()
            if dice == 1:
                print("=========================")
                print("이제 컴퓨터의 차례입니다.")
                print("=========================")
                break
            user_type = input("주사위를 더 굴리시겠습니까? (r(roll)/s(stop)): ")
            should_roll = user.should_roll(user_type)
            if not should_roll:
                break
        print(f"computer total score : {computer.total_score}")
        print(f"{user.name} total score : {user.total_score}")
        if user.is_win():
            print("당신이 이겼습니다.")
            win = True
            break

        print("=========================")
        print("이제 컴퓨터의 차례입니다.")
        print("=========================")
        computer.computer_roll()
        user.tmp_score = 0
        computer.tmp_score = 0

        if computer.is_win():
            print("컴퓨터가 이겼습니다.")
            win = True
            break

if __name__ == "__main__":
    game()