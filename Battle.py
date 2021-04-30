import random
pExp = 12
mobExp = 5
miss = 0
currentHPuser = 60
currentHPmob = 10
attacUser = 2
attacMob = 1


def battle(hp1, hp2, attac1, attac2):
    battleHPuser = hp1
    battleHPmob = hp2
    battleAttacUser = attac1
    battleAttacMob = attac2
    while resultBattle(battleHPuser, battleHPmob, attac1, attac2):
        miss = random.randint(0, 100)
        if miss >= 90:
            battleHPuser -= battleAttacMob
            battleHPmob -= battleAttacUser
        else:
            print('Ты промахнулся')
            battleHPuser -= battleAttacMob


def updateHP(hpUser, hpMob):
    global currentHPuser
    global currentHPmob
    currentHPuser = hpUser
    currentHPmob = hpMob


def resultBattle(hpUser, hpMob, attacUser, attacMob):
    battle = True
    if hpUser > 0:
        print('Игрок жив')
        if hpMob > 0:
            print('Моб жив')
            print('HP игрока', hpUser)
            print('HP моба', hpMob)
            battle = True
            return battle
        else:
            print('Вы победили')
            print('HP игрока', hpUser)
            print('HP моба', hpMob)
            print('Вы получили -', mobExp , 'опыта')
            print('Ваш итоговый опыт -', pExp + mobExp)
            battle = False
            return battle
    else:
        print('Вы проиграли и потеряли', mobExp/2, 'опыта')
        print('Ваш итоговый опыт -', pExp - mobExp/2)
        battle = False
        return battle


battle(currentHPuser, currentHPmob, attacUser, attacMob)
