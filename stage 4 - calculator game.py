import random
import re


def check_name():
    global name
    while True:
        try:
            name = str(input("What is your name?\n"))
            if re.match(r"[A-Z][a-z]{2,19}", name):
                break
            else:
                raise ValueError
        except ValueError:
            print('Incorrect format.')


def safe_results(safe):
    variants = ['yes', 'Yes', 'YES', 'y']
    answer = input()
    level_description = ["(simple operations with numbers 2-9)", "(integral squares 11-29)"]
    if answer in variants:
        saved = open("results.txt", 'a', encoding='utf-8')
        check_name()
        if user_data == 1:
            saved.write(f"\n{name}: {safe}/5 in level {user_data} {level_description[0]}")
        else:
            saved.write(f"\n{name}: {safe}/5 in level {user_data} {level_description[1]}")
        saved.close()
        print('The results are saved in "results.txt".')
        exit()
    else:
        exit()


def game_1(times):
    correct_ans = 0
    while True:
        if times == 5:
            print(f"Your mark is {correct_ans}/5. Would you like to save your result to the file? Enter yes or no.")
            safe_results(correct_ans)
            break
        given = random.sample(range(2, 10), 2)
        oper = random.choice("+-*")
        n1, n2 = given[0], given[1]
        print(n1, oper, n2)
        answer = check_format()
        result = eval(str(n1) + oper + str(n2))
        if answer == result:
            print("Right!")
            times += 1
            correct_ans += 1
        else:
            print("Wrong!")
            times += 1


def game_2(times):
    correct_ans = 0
    while True:
        if times == 5:
            print(f"Your mark is {correct_ans}/5. Would you like to save your result to the file? Enter yes or no.")
            safe_results(correct_ans)
            break
        given = random.randint(11, 29)
        print(given)
        answer = check_format()
        result = given * given
        if answer == result:
            print("Right!")
            times += 1
            correct_ans += 1
        else:
            print("Wrong!")
            times += 1


def check_difficulty(text):
    global user_data
    while True:
        try:
            user_data = int(input(f"{text}"))
            if user_data == 1:
                game_1(0)
            elif user_data == 2:
                game_2(0)
            else:
                raise ValueError
        except ValueError:
            print('Incorrect format.')


def check_format():
    while True:
        try:
            is_num = int(input())
            return is_num
        except ValueError:
            print('Incorrect format.')


msg_1 = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n"""

check_difficulty(msg_1)
