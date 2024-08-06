# Project 1
# Math Question Game

import random

def set_difficulty():
    ch = input('Enter Difficulty "Easy(e) | Medium(m) | Hard(h) | Extreme(ex)": ').lower()

    if ch in ['easy', 'e', '1', 'ea', 'eas']:
        print('Setting Difficulty to "Easy"')
        max_number = 10
        questions_amount = 5
    elif ch in ['medium', 'med', '2', 'me', 'medi', 'mediu']:
        print('Setting Difficulty to "Medium"')
        max_number = 30
        questions_amount = 10
    elif ch in ['hard', 'h', '3', 'ha', 'har']:
        print('Setting Difficulty to "Hard"')
        max_number = 60
        questions_amount = 15
    elif ch in ['extreme', 'ex', '4', 'ext', 'extr', 'extre', 'extrem']:
        print('Setting Difficulty to "Extreme"')
        max_number = 99
        questions_amount = 20
    else:
        print('Invalid input, Defaulting to "Easy" Mode\n')
        max_number = 10
        questions_amount = 5
    return max_number, questions_amount

def gen_prob():
    n1 = random.randint(0, max_number + 1)
    n2 = random.randint(0, max_number + 1)
    operator = random.choice(operators)
    equation = f'{n1} {operator} {n2} '
    answer = eval(equation)
    return equation, answer

operators = ['+', '-', '*', '/', 'sq']
max_number, questions_amount = set_difficulty()
questions = {}

for i in range(questions_amount):
    eq, ans = gen_prob()
    questions[eq] = ans

correct_ans = 0
wrong_ans = 0
for expr, ans in questions.items():
    answer = int(input(f'{expr} = '))
    if answer == ans:
        correct_ans += 1

percentage = float(correct_ans / questions_amount) * 100
print(f'You got {correct_ans}/{questions_amount} questions correct. ({percentage}%)')

if percentage <= 100 and percentage >= 90:
    print('You got A Grade')
elif percentage <= 90 and percentage >= 80:
    print('You got A- Grade')
elif percentage <= 80 and percentage >= 70:
    print('You got B Grade')
elif percentage <= 70 and percentage >= 65:
    print('You got B- Grade')
elif percentage <= 65 and percentage >= 60:
    print('You got C Grade')
elif percentage <= 60 and percentage >= 50:
    print('You got D Grade')
else:
    print('You got F Grade')
