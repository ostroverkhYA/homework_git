print("How much money do you wont?")
number = int(input())
money = (1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
if number >= money[0]:
    for i in range(1, number // money[0]+1):
        number -= money[0]
    print(i, 'banknotes by', money[0])
if number >= money[1]:
    for i in range(1, number // money[1]+1):
        number -= money[1]
    print(i, 'banknotes by', money[1])
if number >= money[2]:
    for i in range(1, number // money[2]+1):
        number -= money[2]
    print(i, 'banknotes by', money[2])
if number >= money[3]:
    for i in range(1, number // money[3]+1):
        number -= money[3]
    print(i, 'banknotes by', money[3])
if number >= money[4]:
    for i in range(1, number // money[4]+1):
        number -= money[4]
    print(i, 'banknotes by', money[4])
if number >= money[5]:
    for i in range(1, number // money[5]+1):
        number -= money[5]
    print(i, 'banknotes by', money[5])
if number >= money[6]:
    for i in range(1, number // money[6]+1):
        number -= money[6]
    print(i, 'banknotes by', money[6])
if number >= money[7]:
    for i in range(1, number // money[7]+1):
        number -= money[7]
    print(i, 'banknotes by', money[7])
if number >= money[8]:
    for i in range(1, number // money[8]+1):
        number -= money[8]
    print(i, 'banknotes by', money[8])
if number >= money[9]:
    for i in range(1, number // money[9]+1):
        number -= money[9]
    print(i, 'banknotes by', money[9])
print('Thanks for using aur ATM  :)')

