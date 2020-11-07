import random
import sys

print('hello')
start_index = sys.argv[1]
last_index = sys.argv[2]
flag = True

num = random.randint(int(start_index), int(last_index))
print(num)
while flag:
    print('Enter guessing number')
    inputNum = input()
    if int(inputNum) == num:
        print('You are genius')
        flag = False
        break
    else:
        print('Guessing Failed')



