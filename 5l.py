import random
def ugad():
    m=[]
    for i in range(5):
        m.append(random.randint(0,10))
    n=int(input('Введите число '))
    if n in m:
        print('Вы угадали число!)')
    else:
        print('Нет такого числа((')
def povtor():
    m = []
    for i in range(10):
        m.append(random.randint(0, 10))
    print('Список:', m)
    print('Повтор. элементы:', sep=' ')
    for i in range(10):
        if m.count(m[i])>1:
            print(m[i], sep=' ')
def dni():
    kv=int(input('сколько дней в неделю вы хотите отдыхать? '))
    if kv>7 or kv<0:
        print('ОШИБКА, введите число от 0 до 7!')
    else:
        kr=7-kv
        ned=('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
        r=[]
        v=[]
        for i in range(kv):
            d=random.choice(ned)
            while d in v:
                d=random.choice(ned)
            v.append(d)
        for i in range(7):
            if ned[i] not in v:
                r.append(ned[i])
        print('Ваши выходные дни:', *v)
        print('Ваши рабочие дни:', *r)
def stud():
    gr1=['Горбунов', 'Епифанова', 'Иванова', 'Королёва', 'Куклина', 'Ларионова', 'Латышева', 'Мельников', 'Никитин', 'Полякова']
    gr2=['Алиева', 'Бережная', 'Власов', 'Денисова', 'Кудрявцев', 'Макрушина', 'Паймина', 'Родченков', 'Салохов', 'Чигина']
    kom=[]
    for i in range(5):
        a = random.choice(gr1)
        while a in kom:
            a = random.choice(gr1)
        kom.append(a)
    for i in range(5):
        a = random.choice(gr2)
        while a in kom:
            a = random.choice(gr2)
        kom.append(a)
    print('1 группа:', *gr1)
    print('2 группа:', *gr2)
    kom.sort()
    komanda=tuple(kom)
    print('спортивная команда:', *komanda)
    print('кол-во участников:', len(komanda))
    st=input('Введите фамилию: ')
    if st in komanda:
        print(st, 'входит в спортивную команду')
    else:
        print(st, 'не входит в спортивную команду')
stud()