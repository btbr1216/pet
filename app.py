# namepet feed play  sleep train quit q
# hunger / 10 energy /15 happiness /20 mood /20
import random

def change(nameofthing, thingtochange, max, randparameters):
    og = thingtochange
    amtincreased = random.randint(randparameters[0], randparameters[1]) + randparameters[2]
    thingtochange += amtincreased
    if thingtochange > max:
        thingtochange = max
        amtincreased = max - og
    final = amtincreased + og
    increaseordecrease = ""
    if amtincreased < 0:
        increaseordecrease = " decreased by "
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

    def feed(self): # only working one (precedent)
        self.hunger = change("hunger", self.hunger, 10, [1, 3, 2])

    def play(self):
        self.energy = change("energy", self.energy, 15, [0, 0, -2])
        self.happiness = change("happiness", self.happiness, 20, [0, 0, 2])

    def sleep(self):
        self.energy = change("energy", self.energy, 15, [0, 0, 2])




pet = Pet("bob", 5, 1, 1, 1)
pet.feed()
pet.play()
