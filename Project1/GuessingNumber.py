import random


def check_guess():
    answer = random.randint(1, 10)
    print(answer)
    try:
        num = int(input('Enter number between 1 to 10'))
        if 0 < num < 11:
            if num == answer:
                return 'You are genius'
            else:
                return 'Try again'
    except ValueError as err:
        return err
