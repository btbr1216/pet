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

def functionforgradualloss(value, secondvaluejustpassing):
    wasoriginallyzero = False
    if value == 0:
        wasoriginallyzero = True
    value -= 1
    if value <= 0:
        return [secondvaluejustpassing, 0, wasoriginallyzero]
    else:
        return [secondvaluejustpassing, value, wasoriginallyzero]

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
            infolist = functionforgradualloss(self.hunger, "hunger")
            self.hunger = infolist(self.hunger)[1]
            return infolist
        elif whichone == 1:
            infolist = functionforgradualloss(self.energy, "energy")
            self.energy = infolist[1]
            return infolist
        elif whichone == 2:
            infolist = functionforgradualloss(self.happiness, "happiness")
            self.happiness = infolist[1]
            return infolist
        elif whichone == 3:
            infolist = functionforgradualloss(self.mood, "mood")
            self.mood = infolist[1]
            return infolist
name = input("Name your pet: ")
pet = Pet(name, 3, 3, 3, 3)

outoflist = {
    "hunger": "/10",
    "energy": "/15",
    "happiness": "/20",
    "mood": "/20"
}

from threading import Thread
from time import sleep
import random

deathdeterminerfromgradualloss = False

def forloop():
    for i in range(4): # put this in a thread too it delays starting
        def decreaseloop():
            num = i
            while True:
                if random.randint(1, 10) == 1:
                    infolist = pet.decreasesomething(num)
                    decreasedby = "1"
                    if infolist[2]:
                        decreasedby = "0"
                    print(name + " lost " + decreasedby + " " + infolist[0] + " and now has " + str(infolist[1]) + outoflist[infolist[0]] + " " + infolist[0])
                    if infolist[1] == 0:
                        print(name + " died")
                sleep(2)
        sleep(random.randint(1, 2))
        
    t = Thread(target=decreaseloop)
    t.start()

t = Thread(target=forloop)
t.start()

while True:
    if deathdeterminerfromgradualloss:
        break
    print("[1] feed")
    print("[2] play")
    print("[3] sleep")
    print("[4] train")
    print("[q] quit")
    for i in pet.getstats():
        print(name + " has " + str(i[0]) + outoflist[i[1]] + " " + i[1])
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