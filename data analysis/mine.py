latter = ['N', 'M', 'Q', 'cw', 'sw', 'hw', 'tw']  # порядок в котром вводят
latter1 = ['M', 'N', 'cw', 'sw', 'hw', 'tw', 'Q']  # нужный порядок
parametrs = list(map(int, input().split()))
data = dict(zip(latter, parametrs))  # данные с правильным порядком
balls_of_activity = {
    'a': data['cw'],
    'b': data['sw'],
    'c': data['hw'],
    'd': data['tw'],
}

if data['M'] <= 0:
    print('Во введённых данных ошибка')
    exit()

if data['N'] <= 0:
    print('Во введённых данных ошибка')
    exit()
if not (
    data['cw'] > 0 and data['sw'] > 0 and data['hw'] > 0 and data['tw'] > 0
):
    print('Во введённых данных ошибка')
    exit()
balls_end = {}
for _ in range(data['N']):
    rating = {'last_name': input(), 'a': [], 'b': [], 'c': [], 'd': []}
    for i in range(data['M']):
        ind = 0
        line = input().split(',')  # ввод оценок ученика
        for key, val in rating.items():
            if key == 'last_name':
                continue
            val.append(int(line[ind]))
            ind += 1
    res = []
    for key, val in rating.items():
        if key == 'last_name':
            continue
        for key1, val1 in balls_of_activity.items():
            for el in val:
                if key1 == key:
                    res.append(el * val1)
                else:
                    continue

    max_rating = 100 * (sum(res) / data['Q'])

    if sum(res) > data['Q']:
        print('Во введённых данных ошибка')
        exit()
    balls_end[rating['last_name']] = max_rating


ball = []
sor_items = dict(sorted(balls_end.items(), key=lambda x: x[1], reverse=True))
for val in sor_items.values():
    ball.append(round(val))
print(max(ball), round(sum(ball) / len(ball)), min(ball))
for ind, (key, val) in enumerate(sor_items.items()):
    if ind <= 2:
        print(f'{key} {round(val)}%')

if round(sum(ball) / len(ball)) <= 50:
    print('Курс усваивается плохо')
else:
    print('Курс усваивается хорошо')
