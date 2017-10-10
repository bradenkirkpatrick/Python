import random


class Person:
    def __init__(self):
        self.name = ""
        self.Class = ""
        self.XP = 0
        self.LVL = 1
        self.STR = 0
        self.INT = 0
        self.CON = 0
        self.ATK = self.STR
        self.mATK = self.INT
        self.DEF = 0
        self.HP = 25
        self.SKILL = 0
        self.STAM = .6
        self.SPELL = 0
        self.MANAp = .7
        self.SKILLp = 0
        self.GOLD = 0
        self.knowlegeLVL = 0

    def setSTR(self, val):
        self.STR += val
        self.ATK = self.STR
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.HP = 25 + 3 * self.CON + 0.1 * self.STR

    def setINT(self, val):
        self.INT += val
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.mATK = self.INT

    def setCON(self, val):
        self.CON += val
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.HP = 25 + 3 * self.CON + 0.1 * self.STR

    def setXP(self, val):
        self.XP += val
        x, i = 0, 0
        while self.XP > x:
            x = 10 * (2**i)
            i += 1
        self.LVL = i

    def setSKILL(self, val):
        self.SKILL += val
        self.STAM = .8 - self.SKILL * .2

    def setSPELL(self, val):
        self.SPELL += val
        self.MANAp = .7 - self.SPELL


class Undead:
    def __init__(self):
        self.name = ""
        self.Class = ""
        self.XP = char.XP
        self.LVL = 0
        self.STR = 0
        self.INT = 0
        self.CON = 0
        self.ATK = self.STR * 1.1 + 5
        self.mATK = self.INT * 1.1 + 5
        self.DEF = 0
        self.HP = 25
        self.GOLD = self.LVL * 2 + random.randint(0, 10)
        self.XPgain = round(2 ** self.LVL + 23)

    def setSTR(self, val):
        self.STR += val
        self.ATK = self.STR
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.HP = 25 + 3 * self.CON + 0.1 * self.STR

    def setINT(self, val):
        self.INT += val
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.mATK = self.INT

    def setCON(self, val):
        self.CON += val
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.HP = 25 + 2 * self.CON + 0.1 * self.STR

    def setXP(self, val):
        self.XP += val
        x, i = 0, 0
        while self.XP > x:
            x = 10 * (2**i)
            i += 1
        self.LVL = i


class Evil:
    def __init__(self):
        self.name = ""
        self.Class = ""
        self.XP = char.XP
        self.LVL = 1
        self.STR = 0
        self.INT = 0
        self.CON = 0
        self.ATK = self.STR * 1.1 + 5
        self.mATK = self.INT * 1.1 + 5
        self.DEF = 0
        self.HP = 25
        self.GOLD = self.LVL * 2 + random.randint(0, 10)
        self.XPgain = round(2 ** self.LVL + 23)

    def setSTR(self, val):
        self.STR += val
        self.ATK = self.STR
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.HP = 25 + 3 * self.CON + 0.1 * self.STR

    def setINT(self, val):
        self.INT += val
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.mATK = self.INT

    def setCON(self, val):
        self.CON += val
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.HP = 25 + 2 * self.CON + 0.1 * self.STR

    def setXP(self, val):
        self.XP += val
        x, i = 0, 0
        while self.XP > x:
            x = 10 * (2**i)
            i += 1
        self.LVL = i


class Orc:
    def __init__(self):
        self.name = ""
        self.Class = ""
        self.XP = char.XP
        self.LVL = 0
        self.STR = 0
        self.INT = 0
        self.CON = 0
        self.ATK = self.STR * 1.1 + 5
        self.mATK = self.INT * 1.1 + 5
        self.DEF = 0
        self.HP = 25
        self.GOLD = self.LVL * 2 + random.randint(0, 10)
        self.XPgain = round(2 ** self.LVL + 23)

    def setSTR(self):
        self.STR += char.LVL * 2
        self.ATK = self.STR
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.HP = 25 + 3 * self.CON + 0.1 * self.STR

    def setINT(self):
        self.INT += char.LVL * 2
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.mATK = self.INT

    def setCON(self):
        self.CON += char.LVL * 2
        self.DEF = self.INT * .05 + self.STR * .05 + self.CON * .1
        self.HP = 25 + 2 * self.CON + 0.1 * self.STR

    def setXP(self, val):
        self.XP += val
        x, i = 0, 0
        while self.XP > x:
            x = 10 * (2**i)
            i += 1
        self.LVL = i + random.randint(-2, 2)


def save(char):  # CHAR IS CLASS PERSON
    file = open('save.txt', 'w')
    file.write(char.name + ',{0},{1},{2},{3},{4},{5},{6},{7}'.format(char.Class, char.STR, char.INT, char.CON, char.XP, char.GOLD, char.SKILL, char.SPELL))
    file.close()


def load(char):
    file = open('save.txt', 'r')
    char.name, char.Class, STR, INT, CON, XP, GOLD, SKILL, SPELL = (file.read()).split(",")
    char.Class = int(char.Class)
    char.setXP(int(XP))
    char.setSTR(int(STR))
    char.setINT(int(INT))
    char.setCON(int(CON))
    char.setSTR(int(STR))
    char.setINT(int(INT))
    char.GOLD = (int(GOLD))
    char.setSKILL(int(SKILL))
    char.setSPELL(int(SPELL))
    file.close()
char = Person()
load(char)
Undead = Undead()
Evil = Evil()
Orc = Orc()
LVL = char.LVL
Evil.LVL = LVL
Orc.LVL = LVL
Undead.LVL = LVL
while True:
    print('New game(1) or load save(2)')
    q = int(input("Enter a number: "))
    if q == 1:
        name = input("what is your name: ")
        while True:
            def set_x_to_one():
                global x
            print('what would you like to be, warrior = 1 wizard = 2 thief = 3')
            y = 'hi'
            STR = random.randint(3, 5)
            INT = random.randint(3, 5)
            CON = random.randint(3, 5)
            char = Person()
            char.name = name

            x = int(input("Enter a number: "))
            if x == 1:
                y = "warrior"
                STR += 5
                char.setSTR(STR)
                char.setINT(INT)
                char.setCON(CON)
                char.Class = x
                char.SKILL = 1
                char.SPELL = 1
                save(char)
                break
            elif x == 2:
                y = "wizard"
                INT += 5
                char.setSTR(STR)
                char.setINT(INT)
                char.setCON(CON)
                char.Class = x
                char.SKILL = 1
                char.SPELL = 1
                save(char)
                break
            elif x == 3:
                y = "thief"
                CON += 5
                char.setSTR(STR)
                char.setINT(INT)
                char.setCON(CON)
                char.Class = x
                char.SKILL = 1
                char.SPELL = 1
                save(char)
                break
        if not x == 2:
            print("You have become a " + y)
        else:
            print("Your a " + y + ", " + name)
        break
    elif q == 2:
        print('good your back again')
        break


print('LVL = ' + str(char.LVL))
print("XP = {0}%".format(char.XP / (10 * (2 ** char.LVL)) * 100))
print('STR = ' + str(char.STR))
print('INT = ' + str(char.INT))
print('CON = ' + str(char.CON))
print('Gold = ' + str(char.GOLD))
print('What do you want to do, "looks at map"')
print('')

while True:
    char.setXP(val=0)
    b = int(input("check map(1) Check stats(2) Exit game(3): "))
    if b == 1:
        while True:
            h = int(input("Go to, AlUmineaum city(1) AlUmineaum Graveyard(2) The mushroom forest(3) The municipality of scholar(4) stop looking at map(5): "))
            if h == 1:
                z = int(input("Fight off invaders(1) go to shop(2) Leave city(3): "))
                if z == 1:
                    y = 1
                    Evil.setSTR(2 * char.LVL)
                    Evil.setINT(2 * char.LVL)
                    Evil.setCON(2 * char.LVL)
                    STAM = char.STAM
                    NAMEe = random.randint(1, 3)
                    SKILL = char.SKILL
                    HPe = Evil.HP
                    ATKe = Evil.ATK
                    mATKe = Evil.mATK
                    DEFe = Evil.DEF
                    MANA = char.MANAp
                    HP = char.HP
                    ATK = char.ATK
                    mATK = char.mATK
                    DEF = char.DEF
                    while True:
                        if y == 1:
                            x = int(input(
                                "(1)Melee Attack (2)Spec. Melee Attack (3)Cast Magic Attack (4)Cast Magic Spell: "))
                            if x == 1:
                                HPe -= ATK
                                STAM += .1
                                MANA += .1
                            elif x == 2:
                                while True:
                                    if char.SKILL == 1:
                                        HPe -= 1.25 * ATK
                                    if char.SKILL == 2:
                                        r = int(input("(1)power strike (2)vampiric stab: "))
                                        if r == 1:
                                            HPe -= 1.5 * ATK
                                        elif r == 2:
                                            HPe -= .75 * ATK
                                            HP += .5 * ATK
                            elif x == 3:
                                HPe -= mATK
                                STAM += .1
                                MANA += .1
                            elif x == 4:
                                if MANA >= 1:
                                    HPe -= char.SPELL
                                    MANA -= 1 - char.MANAp
                                elif MANA <= 1:
                                    MANA -= 1 - char.MANAp
                                    print('"spell fissled"')
                            if HPe <= 0:
                                print('You are victorious')
                                char.setXP(Evil.XPgain)
                                char.GOLD += Evil.GOLD
                                if not char.LVL == LVL:
                                    print('You have leveled up from ' + str(LVL) + ' to ' + str(char.LVL))
                                    char.SKILLp += 5
                                    LVL = char.LVL
                                break
                            elif HPe >= 0:
                                print('You have HP:')
                                print(HP)
                                print('Your enemy has HP:')
                                print(HPe)
                            if NAMEe == 1:
                                HP -= ATKe
                            elif NAMEe == 2:
                                HP -= mATKe
                            elif NAMEe == 3:
                                HP -= ATKe
                                HPe += 1 / 3 * ATKe
                            if HP <= 0:
                                print('You have been defeated')
                                char.XP += Undead.XPgain * (1 / 3)
                                break
                    break
                elif z == 2:
                    print('UNFINISHED')
                    break
                elif z == 3:
                    break
            elif h == 2:
                z = int(input("Fight against the necromancer's army(1) go to general p's camp(2)Leave city(3): "))
                if z == 1:
                    y = 1
                    Undead.setSTR(2 * char.LVL)
                    Undead.setINT(2 * char.LVL)
                    Undead.setCON(2 * char.LVL)
                    STAM = char.STAM
                    NAMEe = random.randint(1, 3)
                    SKILL = char.SKILL
                    HPe = Undead.HP
                    ATKe = Undead.ATK
                    mATKe = Undead.mATK
                    DEFe = Undead.DEF
                    MANA = char.MANAp
                    HP = char.HP
                    ATK = char.ATK
                    mATK = char.mATK
                    DEF = char.DEF
                    while True:  # BATTLE CODE <<<-----------------
                        if y == 1:
                            x = int(input(
                                "(1)Melee Attack (2)Spec. Melee Attack (3)Cast Magic Attack (4)Cast Magic Spell: "))
                            if x == 1:
                                HPe -= ATK
                                STAM += .1
                                MANA += .1
                            elif x == 2:
                                while True:
                                    if char.SKILL == 1:
                                        HPe -= 1.25 * ATK
                                    if char.SKILL == 2:
                                        r = int(input("(1)power strike (2)vampiric stab: "))
                                        if r == 1:
                                            HPe -= 1.5 * ATK
                                        elif r == 2:
                                            HPe -= .75 * ATK
                                            HP += .5 * ATK
                            elif x == 3:
                                HPe -= mATK
                                STAM += .1
                                MANA += .1
                            elif x == 4:
                                if MANA >= 1:
                                    HPe -= char.SPELL
                                    MANA -= 1 - char.MANAp
                                elif MANA <= 1:
                                    MANA -= 1 - char.MANAp
                                    print('"spell fissled"')
                            if HPe <= 0:
                                print('You are victorious')
                                char.setXP(Undead.XPgain)
                                char.GOLD += Undead.GOLD
                                if not char.LVL == LVL:
                                    print('You have leveled up from ' + str(LVL) + ' to ' + str(char.LVL))
                                    char.SKILLp += 5
                                    LVL = char.LVL
                                break
                            elif HPe >= 0:
                                print('You have HP:')
                                print(HP)
                                print('Your enemy has HP:')
                                print(HPe)
                            if NAMEe == 1:
                                HP -= ATKe
                            elif NAMEe == 2:
                                HP -= mATKe
                            elif NAMEe == 3:
                                HP -= ATKe
                                HPe += 1 / 3 * ATKe
                            if HP <= 0:
                                print('You have been defeated')
                                char.XP += Undead.XPgain * (1 / 3)
                                break
                            elif y == 3:
                                break
                elif z == 2:
                    while True:
                        print(char.GOLD)
                        t = int(input("get trained skills(1) Leave camp(2): "))
                        if t == 1:
                            u = int(input("get trained vampiric stab(1) Leave camp(2): "))
                            if u == 1:
                                if char.GOLD >= 250:
                                    char.GOLD -= 250
                                    if char.SKILL == 1:
                                        char.SKILL += 1
                                        break
                                    else:
                                        print('Already learned, cant relearn skill')
                            elif u == 2:
                                break
                        elif t == 2:
                            break

                elif z == 3:
                    break
            elif h == 3:
                z = int(input("Attack the orcs(1) go to the witch doctor's shop(2) Leave city(3): "))
                if z == 1:
                    y = 1
                    if char.LVL > 10:
                        HPe = 25 + 2 * 20
                        ATKe = 2 * 10 + random.randint(-2, 2)
                        mATKe = 2 * 10 + random.randint(-2, 2)
                    elif char.LVL <= 10:
                        HPe = Orc.HP
                        ATKe = Orc.ATK
                        mATKe = Orc.mATK
                    NAMEe = random.randint(1, 3)
                    MANA = char.MANAp
                    HP = char.HP
                    ATK = char.ATK
                    mATK = char.mATK
                    DEF = char.DEF
                    SKILL = char.SKILL
                    STAM = char.STAM
                    while True:  # BATTLE CODE <<<-----------------
                        if y == 1:
                            x = int(input(
                                "(1)Melee Attack (2)Spec. Melee Attack (3)Cast Magic Attack (4)Cast Magic Spell: "))
                            if x == 1:
                                HPe -= ATK
                                STAM += .1
                                MANA += .1
                            elif x == 2:
                                while True:
                                    if char.SKILL == 1:
                                        HPe -= 1.25 * ATK
                                    if char.SKILL == 2:
                                        r = int(input("(1)power strike (2)vampiric stab: "))
                                        if r == 1:
                                            HPe -= 1.5 * ATK
                                        elif r == 2:
                                            HPe -= .75 * ATK
                                            HP += .5 * ATK
                            elif x == 3:
                                HPe -= mATK
                                STAM += .1
                                MANA += .1
                            elif x == 4:
                                if MANA >= 1:
                                    HPe -= char.SPELL
                                    MANA -= 1 - char.MANAp
                                elif MANA <= 1:
                                    MANA -= 1 - char.MANAp
                                    print('"spell fissled"')
                            if HPe <= 0:
                                print('You are victorious')
                                char.setXP(Orc.XPgain)
                                if char.LVL >=10:
                                    char.GOLD += 10 * 2 + random.randint(0, 10)
                                else:
                                    char.GOLD += Orc.GOLD
                                if not char.LVL == LVL:
                                    print('You have leveled up from ' + str(LVL) + ' to ' + str(char.LVL))
                                    char.SKILLp += 5
                                    LVL = char.LVL
                                break
                            elif HPe >= 0:
                                print('You have HP:' + HP)
                                print('Your enemy has HP:' + HPe)
                            if NAMEe == 1:
                                HP -= ATKe
                            elif NAMEe == 2:
                                HP -= mATKe
                            elif NAMEe == 3:
                                HP -= ATKe
                                HPe += 1 / 3 * ATKe
                            if HP <= 0:
                                print('You have been defeated')
                                char.XP += Undead.XPgain * (1 / 3)
                                break
                            elif y == 3:
                                break
                elif z == 2:
                    print('UNFINISHED')
                    break
                elif z == 3:
                    break
            elif h == 4:
                if char.knowlegeLVL == 0:
                    char.knowlegeLVL += 1
                    print('"Take the book dont let them have it, The book will tell you every thing"')
                    print('(the book tells you about the omniverses, and the peace lords.)')
                    print('you are ambush by a man with 23 cromeasones')
                    y = 1
                    HPe = 100
                    ATKe = 12
                    DEFe = 0
                    MANA = char.MANAp
                    HP = char.HP
                    ATK = char.ATK
                    mATK = char.mATK
                    DEF = char.DEF
                    SKILL = char.SKILL
                    STAM = char.STAM
                    while True:  # BATTLE CODE <<<-----------------
                        if y == 1:
                            x = int(input(
                                "(1)Melee Attack (2)Spec. Melee Attack (3)Cast Magic Attack (4)Cast Magic Spell: "))
                            if x == 1:
                                HPe -= ATK
                                STAM += .1
                                MANA += .1
                            elif x == 2:
                                while True:
                                    if char.SKILL == 1:
                                        HPe -= 1.25 * ATK
                                    if char.SKILL == 2:
                                        r = int(input("(1)power strike (2)vampiric stab: "))
                                        if r == 1:
                                            HPe -= 1.5 * ATK
                                        elif r == 2:
                                            HPe -= .75 * ATK
                                            HP += .5 * ATK
                            elif x == 3:
                                HPe -= mATK
                                STAM += .1
                                MANA += .1
                            elif x == 4:
                                if MANA >= 1:
                                    HPe -= char.SPELL
                                    MANA -= 1 - char.MANAp
                                elif MANA <= 1:
                                    MANA -= 1 - char.MANAp
                                    print('"spell fissled"')
                            if HPe <= 0:
                                print('You are victorious')
                                char.setXP(Undead.XPgain)
                                char.GOLD += Undead.GOLD
                                if not char.LVL == LVL:
                                    print('You have leveled up from ' + str(LVL) + ' to ' + str(char.LVL))
                                    char.SKILLp += 5
                                    LVL = char.LVL
                                break
                            elif HPe >= 0:
                                print('You have HP:')
                                print(HP)
                                print('Your enemy has HP:')
                                print(HPe)
                            HP -= ATKe
                            if HP <= 0:
                                print('You have been defeated')
                                char.XP += Undead.XPgain * (1 / 3)
                                break
                z = int(input("Fight for king fillip's army(1) go to shop(2)"
                              " go to wizard's tower(3) go to library(4) Leave city(5): "))
                if z == 1:
                    print('UNFINISHED')
                    break
                elif z == 2:
                    print('UNFINISHED')
                    break
                elif z == 3:
                    print('UNFINISHED')
                    break
                elif z == 4:
                    print('UNFINISHED')
                    break
                elif z == 5:
                    break
            elif h == 5:
                break
    elif b == 2:
        while True:
            print('LVL = ' + str(char.LVL))
            print("XP = {0}%".format(char.XP / (10 * (2 ** char.LVL) * 100)))
            print('STR = ' + str(char.STR))
            print('INT = ' + str(char.INT))
            print('CON = ' + str(char.CON))
            if char.SKILLp > 0:
                print('do you what to add skill points:' + ' you have' + str(char.SKILLp) + "skill points")
                w = int(input('Yes(1) No, exit stats(2)'))
                if w == 1:
                    while True:
                        e = int(input('Add STR(1) Add INT(2) Add CON(3) cancel(4)'))
                        if e == 1:
                            if char.SKILLp > 0:
                                char.STR += 1
                                char.SKILLp -= 1
                                if char.SKILLp > 0:
                                    print('You have ' + str(char.SKILLp) + 'Left')
                                elif char.SKILLp < 1:
                                    print('you have no skill points left')
                            elif char.SKILLp < 1:
                                break
                        elif e == 2:
                            if char.SKILLp > 0:
                                char.INT += 1
                                char.SKILLp -= 1
                                if char.SKILLp > 0:
                                    print('You have ' + str(char.SKILLp) + 'Left')
                                elif char.SKILLp < 1:
                                    print('you have no skill points left')
                            elif char.SKILLp < 1:
                                break
                        elif e == 3:
                            if char.SKILLp > 0:
                                char.CON += 1
                                char.SKILLp -= 1
                            elif char.SKILLp < 1:
                                break
                        elif e == 4:
                            break
                elif w == 2:
                    break
            else:
                break

    elif b == 17:
        if char.LVL <= 20:
            print("nothing happened")
        elif char.LVL >= 20:
            print('You open a map of a unknown land called "IaDean"')
    elif b == 3:
        save(char)
        break
