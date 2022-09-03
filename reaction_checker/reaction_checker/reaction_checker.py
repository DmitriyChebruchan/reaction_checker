# function checks reaction time of user
import time
import math


def reaction_checker():
    print('\n\n\nПривет! Это программа для тестирования реакции.')
    time.sleep(3) 
    print('Сейчас будет запущен тест 5 раз по каждому из 4 временных отрезков.')
    time.sleep(3)
    print('Временные отрезки: 2, 3, 4, 5 секунд.\n')
    time.sleep(3)
    print('Чтобы запустить таймер или остановить таймер нажмите Enter на клавиатуре.')
    input('\nОтрепетируем. \nНажмите Enter один раз.\n')
    print('\nХорошо! Начнем тест.\n')
    time.sleep(3)

    result = {}
    for i in range(1, 5):
        collected_results = []
        for n in range(5):
            collected_results.append(checker(i+1, n+1))
        avrg = math.fsum(collected_results)/len(collected_results)
        result[str(i+1)] = round(avrg, 3)
        print('Тестирование реации на период {} секунд заверщено.'.format(i+1))
        print('____________________________________________________________')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('____________________________________________________________')
    for key, value in result.items():
        print('Среднее время реации на период {} секунд: {} секунд.'.format(key, value))
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
    print("Сейчас мы тестируем период {} секунд.".format(time_period))
    print('Номер текущей поптыки - {} из 5\n'.format(try_number))
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
