"""

https://urban-university.ru/members/courses/course999421818026/20231115-0000domasnee-zadanie-po-teme-formatirovanie-strok-370188502527

"""
#Значения переменных заданы вручную
# Использование %:
team1_num = 5
print("В команде Мастера кода участников: %s ! " % (team1_num))

team2_num = 6
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

#Использование format():

score_2 = 42
print("Команда Волшебники данных решила задач: {0} !".format(score_2))

team1_time= 18015.2
print('Волшебники данных решили задачи за {} с !'.format(team1_time))

#Использование f-строк:
score_1, score_2 = 40,42

print(f"Команды решили {score_1} и {score_2} задач.")

challenge_result = 'Мастера кода'
print(f"Результат битвы: победа команды \"{challenge_result}\" с результатом {score_2}!")

tasks_total, time_avg = 82, 350.4
print(f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")

