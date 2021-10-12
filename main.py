import random
from data import data


def select_person():
    person = random.choice(data)
    return person


def display(account):
    name = account['name']
    followers = account['follower_count']
    description = account['description']
    country = account['country']
    print(name + '\n' + description + '\n' + country + '\n')
    return followers


def game():
    number_1 = display(select_person())
    number_2 = display(select_person())
    option = int(input('Who has more followers ? 1 or 2: '))
    if option == 1 and number_1 >= number_2:
        return f'You are right.'
    elif option == 2 and number_2 >= number_1:

        return f'You are right.'
    else:
        return 'Wrong'


flag = True
count = 0
while flag:
    result = game()
    if result == 'Wrong':
        print(f'Your score was {count}')
        flag = False
    else:
        count += 1
        print(result)
        print(f'Score: {count}\n')
