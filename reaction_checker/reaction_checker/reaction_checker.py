# function checks reaction time of user
import time
import math


# function returns updated list of elements in random order from input list
def randomize_list(input_list):
    import random
    output_list = []
    while len(input_list) > 0:
        element = random.choice(input_list)
        output_list.append(element)
        input_list.remove(element)
    return output_list



def reaction_checker():
    instructions()

    test_run()
    list_of_numbers = randomize_list([2, 3, 4, 5] * 4) 

    result = {}

    collected_results = {2: [], 3: [], 4: [], 5: []}

    for n in range(len(list_of_numbers)):
        collected_results[list_of_numbers[n]].append(checker(list_of_numbers[n], n+1))
  
    tau = calculate_tau(result)
    sigma = sigma_calculator(result, tau)
    options = {'Холерик': [0.7, 0.8],
               'Сангвиник': [0.8, 0.9],
               'Флегматик': [0.9, 1],
               'Меланхолик': [1, 1.1]}
    for key, value in options.items():
        if value[0] <= tau <= value[1]:
            print('Ваш тип темперамента - {}'.format(key))
            break
    print('_________________________________________________________\n')


# function that prints instuctions
def instructions():
    print('''
    Привет! Это программа для тестирования реакции.
    Сейчас будет запущен тест 5 раз по каждому из 4 временных отрезков.
    Временные отрезки: 2, 3, 4, 5 секунд.
    Чтобы запустить таймер или остановить таймер нажмите Enter на клавиатуре.
    ''')


# function that runs the test run
def test_run():
    input('\nОтрепетируем. \nНажмите Enter один раз.\n')
    print('\nХорошо! Начнем тест.\n')
    time.sleep(3)


def sigma_calculator(result, tau):
    sigma = {}
    for key, value in result.items():
        element = value/int(key) - tau
        sigma[key] = element
    print('Сигма: {}'.format(sigma))
    return sigma


def calculate_tau(result):
    tau = sum([x/2 for x in result.values()])/4
    print('тау: {}'.format(tau))
    return tau


def checker(time_period, try_number):
    print('Номер текущей поптыки - {} из 20\n'.format(try_number))
    print('Нажмите Enter на клавиатуре, чтобы запустить таймер.')
    print('Нажмите ее снова, чтобы остановить таймер через {} секунд.'.format(time_period))
    input()
    print('Таймер запущен.')
    start = time.time()
    input()
    stop = time.time()
    print('Таймер остановлен.')
    print('Ваше время реакции записана. Переходим к следующей попытке.')
    print('_________________________________________________________\n\n\n')
    reaction_time = stop - start
    print('Ваше время реакции: {} секунд.'.format(reaction_time))
    return reaction_time
