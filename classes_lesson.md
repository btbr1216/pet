# Lesson: Classes in Python



A **class** is a blueprint. An **object** is a thing built from that blueprint.

Think of a video game. The game has one idea of what a "Hero" is: every hero has a name, some gold, health points (HP) and a backpack. But the game can have many heroes at once. Each one has its **own** name, gold and HP.

| Word | Meaning | Game example |
| --- | --- | --- |
| Class | The blueprint | `Hero` |
| Object / instance | One thing built from the blueprint | `athena`, `leo` |
| Attribute | A piece of data an object stores | `athena.hp`, `athena.money` |
| Method | A function that belongs to the class | `athena.buy("Bow", 120)` |
| `__init__` | The setup method that runs when an object is created | Gives a new hero their starting gold and HP |
| `self` | "This particular object" | Inside `buy`, `self` is whichever hero is shopping |

**Quick check:** Ask students to name a class and three attributes from something in real life (for example, a `Dog` with `name`, `breed`, `age`).

---

## Part 2: Anatomy of a class (15 min)

```python
class Hero:                                  # 1. the class name (Capitalized)
    def __init__(self, name, money, hp=100): # 2. setup method, runs on creation
        self.name = name                     # 3. attributes saved on "self"
        self.money = money
        self.hp = hp

    def potion(self):                        # 4. a method - always takes self first
        self.hp += 10

athena = Hero("Athena", 500)                 # 5. create an object
athena.potion()                              # 6. call a method with a dot
print(athena.hp)                             # 110
```

### What is `self`, really?

When you write `athena.potion()`, Python quietly turns it into:

```python
Hero.potion(athena)
```

So `self` **is** `athena` during that call. If you call `leo.potion()`, then `self` is `leo`. That's how one method can work for every hero.

**Rule of thumb:** Every method written inside a class takes `self` as its first parameter. Anything you want the object to remember must be saved as `self.something`.

---


```python
class Calculator():
     def add(x,y):
           print(x + y)
           return x + y
     def add_many(list):
           print(sum(list))
           return sum(list)
     def subtract(list):
           return list

Calculator.add(5,6)

class Hero:
    def __init__(self, name, money, inventory=[], hp):
        self.name = name
        self.money = money
        self.inventory = inventory
        self.hp = 100
        self.attack = 15
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
    def potion(self):
         self.hp += 10
    def attack(self, goblin):
         goblin.HP -= self.attack
def create_hero(name, money, inventory):
     x = Hero(name, money, inventory)
     return x
#create new instance
Athena = Hero("Athena", 500, ["child", "child2"])
Athena.buy("another Child")
Leo = ("Leo", 0, ["Sword"])

print(Athena.inventory)
```
