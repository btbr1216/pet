# namepet feed play  sleep train quit q
# hunger / 10 energy /15 happiness /20 mood /20
import random

def change(nameofthing, thingtochange, max, randparameters):
    og = thingtochange
    amtincreased = random.randint(randparameters[0], randparameters[1]) + randparameters[2]
    thingtochange += amtincreased
    if thingtochange > max:
        amtincreased = max - og
    if thingtochange < 0:
        amtincreased = 0 - og
    final = amtincreased + og
    increaseordecrease = ""
    if amtincreased < 0:
        increaseordecrease = " decreased by "
        amtincreased *= -1
    else:
        increaseordecrease = " increased by "
    print(nameofthing + increaseordecrease + str(amtincreased) + " and is now " + str(final))
    return final

class Pet:
    def __init__(self, name, hunger, energy, happiness, mood):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.mood = mood

    def feed(self):
        self.hunger = change("hunger", self.hunger, 10, [1, 3, 2])

    def play(self):
        self.energy = change("energy", self.energy, 15, [0, 0, -2])
        self.happiness = change("happiness", self.happiness, 20, [0, 0, 2])
        if self.energy == 0:
            return True

    def sleep(self):
        self.energy = change("energy", self.energy, 15, [0, 0, 5])

    def train(self):
        self.energy = change("energy", self.energy, 15, [0, 0, -2])
        self.mood = change("mood", self.mood, 20, [0, 0, 2])
        if self.energy == 0:
            return True

    def getstats(self):
        return [[self.hunger, "hunger"], [self.energy, "energy"], [self.happiness, "happiness"], [self.mood, "mood"]]

    def decreasesomething(self, whichone):
        if whichone == 0:
            self.hunger -= 1
            return ["hunger", self.hunger]
        elif whichone == 1:
            self.energy -= 1
            return ["energy", self.energy]
        elif whichone == 2:
            self.happiness -= 1
            return ["happiness", self.happiness]
        elif whichone == 3:
            self.mood -= 1
            return ["mood", self.mood]

name = input("Name your pet: ")
pet = Pet(name, 5, 1, 1, 1)

from threading import Thread
from time import sleep
import random

for i in range(4):
    def decreaseloop():
        num = i
        while True:
            if random.randint(1, 10) == 1:
                thinglost = pet.decreasesomething(num)
                print(name + " lost 1 " + thinglost[0] + " and now has " + str(thinglost[1]) + " " + thinglost[0])
            sleep(2)
    sleep(random.randint(1, 2))
        
    t = Thread(target=decreaseloop)
    t.start()


while True:
    print("[1] feed")
    print("[2] play")
    print("[3] sleep")
    print("[4] train")
    print("[q] quit")
    for i in pet.getstats():
        print(name + " has " + str(i[0]) + " " + i[1])
    choice = input("input: ")
    death = False
    if choice == "1":
        death = pet.feed()
    elif choice == "2":
        death = pet.play()
    elif choice == "3":
        death = pet.sleep()
    elif choice == "4":
        death = pet.train()
    elif choice == "q":
        print("quitting")
        break
    if death:
        print(name + " died")
        break