# function checks reaction time of user
import time
from playsound import playsound

START_SOUND = '/Users/dmitriychebruchan/reaction_checker/sound/start.wav'
FINISH_SOUND = '/Users/dmitriychebruchan/reaction_checker/sound/finish.wav'


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

    # running test
    test_run()

    # collect results of tests
    list_of_numbers = randomize_list([2, 3, 4, 5] * 4) 
    collected_results = {2: [], 3: [], 4: [], 5: []}
    for n in range(len(list_of_numbers)):
        collected_results[list_of_numbers[n]].append(checker(list_of_numbers[n], n+1))
    print(collected_results)

    # calculate tau
    tau = calculate_tau(collected_results)
    print(tau)

    # calculate sima
    sigma = sigma_calculator(collected_results, tau)
    print(sigma)

    # show temperament
    show_temperament(tau)


def show_temperament(tau):
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

    # showing the sounds
    input('\nОтрепетируем. \nНажмите Enter один раз, чтобы начать.\n')
    playsound(START_SOUND)
    input('Это был звук старта.\n Нажмите Enter, чтобы услышать звук окончания.')
    playsound(FINISH_SOUND)
    print('\nХорошо! Начнем тестовый прогон.\n')
    time.sleep(2)

    # test run
    input('Нажимайте Enter, чтобы запустить таймер.')
    start = time.time()
    playsound(START_SOUND)
    print('Тест запущен.\n')
    input('Нажимайте Enter снова, чтобы остановить таймер.')
    finish = time.time()
    time_period = round(start - finish, 6)
    playsound(FINISH_SOUND) 
    print('Таймер остановлен.\nТестовый прогон завершен.\n')
    print('Период между нажатиями составил {} секунд(ы).\n'.format(time_period))
    print('_________________________________________________________\n\n\n')
    time.sleep(5)


def sigma_calculator(result, tau):
    sigma = {}
    for key, value in result.items():
        element = sum(value)/5/int(key) - tau
        sigma[key] = element
    print('Сигма: {}'.format(sigma))
    return sigma


def calculate_tau(result):

    avg_div_by_2 = {}
    for key, value in result.items():
        avg_div_by_2[key] = sum(value)/10
    
    list_of_values = []
    for key, value in avg_div_by_2.items():
        list_of_values.append(value)

    tau = sum(list_of_values)/4
    return tau


def checker(time_period, try_number):
    print('Номер текущей поптыки - {} из 20\n'.format(try_number))
    
    input('Готовы?\nНажмите Enter, чтобы прослушать нужный период.\n')
    play_sample(time_period)

    print('Ваша очередь. \nНажмите Enter на клавиатуре, чтобы запустить таймер.')
    print('Нажмите ее снова, чтобы остановить таймер.\n Повторяем...\n')
    input()
    start = time.time()
    playsound(START_SOUND)
    print('Таймер запущен.')

    input()
    stop = time.time()
    playsound(FINISH_SOUND)
    print('Таймер остановлен.')

    reaction_time = round(stop - start, 6)
    print('Время реакции записано.\n')
    print("_" * 80 +'\n\n\n')
    return reaction_time


# function "sample"  plays start  and finish sound with sleep time_period
# seconds
def play_sample(time_period):
    print('Слушаем...')
    time.sleep(1)
    playsound(START_SOUND)
    time.sleep(time_period)
    playsound(FINISH_SOUND)
    print('Ваша очередь.\n\n')
