from random  import randint
from Team import *

printActionDescription = True

def dprint(s):
    if printActionDescription:
        print(s)

#Constants for Mage Type        
manaCost = 20
manaRecovery = 30


class Character(object):
    def __init__(self):
        self.name = ''
        self.maxhp = 1000
        self.hp = 1000
        self.str = 0
        self.maxmana = 0
        self.mana = 0
        self.cost = 9999999999
        self.alive = True

    def act(self,myTeam,enemy):
        return

    def gotHurt(self,damage):
        if damage >= self.hp:
            self.hp = 0
            self.alive = False
            dprint(self.name + ' died!')
        else:
            self.hp -= damage
            dprint(self.name +
                   f' hurt with remaining hp {self.hp}.')

    

class Fighter(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Fighter'
        self.maxhp = 1200
        self.hp = 1200
        self.str = 100
        self.cost = 100

    def act(self,myTeam,enemy):
        target = randAlive(enemy)
        dprint(f'Hurt enemy {target} by damage {self.str}.')
        enemy[target].gotHurt(self.str)
  

class Mage(Character):
    def __init__(self):
        super().__init__()
        self.name = 'Mage'
        self.maxmana = 50
        self.mana = 50
        self.hp = 800
        self.cost = 200
        self.int = 400

    def cast(self,myTeam,enemy):
        self.mana -= manaCost
        target = randAlive(enemy)
        dprint(f'Strike enemy {target} with spell')
        enemy[target].gotHurt(self.int)
        
    def act(self,myTeam,enemy):
        if self.mana < manaCost:
            self.mana += manaRecovery
            dprint(f'Mana recover to {self.mana}.')
        else:
            self.cast(myTeam,enemy)

class Berserker(Fighter):
    def __init__(self):
        super().__init__()
        self.name = 'Berserker'
        self.cost = 200

    def act(self,myTeam,enemy):
        if self.hp <= (self.maxhp//2):
            self.str = 200
            dprint('Berserk mode! Attack double!')
        else:
            self.str = 100
        super().act(myTeam,enemy)
        
class ArchMage(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'ArchMage'
        self.cost = 600

    def kaboom(self,myTeam,enemy):
        self.int = 800
        self.mana -= manaCost
        dprint(f'cast Kaboom ! (Damage({self.int}) to every enemy!')
        for i in enemy:
            i.gotHurt(self.int)

    def cast(self,myTeam,enemy):
        if sum(i.alive for i in myTeam) ==1:
            self.kaboom(myTeam,enemy)
        else:
            super().cast(myTeam,enemy)

class Necromancer(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'Necromancer'
        self.cost = 400

    def raiseDead(self,myTeam):
        self.mana -= manaCost
        target = randDeath(myTeam)
        dprint(f'Reving member {target} with hp {myTeam[target].maxhp//2}.')
        myTeam[target].hp = myTeam[target].maxhp//2
        myTeam[target].alive == True
            
    def cast(self,myTeam,enemy):
        if min(i.alive for i in myTeam) == 0:
            self.raiseDead(myTeam)
        else:
            super().cast(myTeam,enemy)

class Dragon(Mage):
    def __init__(self):
        super().__init__()
        self.name = 'Dragon'
        self.hp = 2200
        self.cost = 700
        self.int = 700

    def cast(self,myTeam,enemy):
        self.mana -= manaCost
        target = randAlive(enemy)
        dprint(f'Burn enemy {target} with fire')
        enemy[target].gotHurt(self.int)



