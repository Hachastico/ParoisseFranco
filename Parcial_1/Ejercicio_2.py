from queue_ import Queue
from list_ import List
from super_heroes_data import superheroes

class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"Name: {self.name}, Alias: {self.alias}, Real Name: {self.real_name}, Villain: {self.is_villain}, First Appearance: {self.first_appearance}"

list_superhero = List()

for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.append(hero)

def order_by_name(item):
    return item.name

def order_by_real_name(item):
    return item.real_name

def order_by_first_appearance(item):
    return item.first_appearance

print("A")
#A
list_superhero.add_criterion("name", order_by_name)
list_superhero.sort_by_criterion("name")
list_superhero.show()
print()
print("B")
#B
index_thing = list_superhero.search("The Thing", "name")
if index_thing is not None:
    print("The Thing esta en la posicion:",{index_thing})

index_rock = list_superhero.search("Rocket Raccoon", "name")
if index_rock is not None:
    print("Rocket Raccoon esta en la posicion:",{index_rock})

print()
print("C")
#C
for hero in list_superhero:
    if hero.is_villain:
        print(hero)
print()
print("D")
#D
villain_queue = Queue()
for hero in list_superhero:
    if hero.is_villain:
        villain_queue.arrive(hero)

aux_villain_queue = Queue() #Para evitar modificar la queue original
while villain_queue.size() > 0:
    villain = villain_queue.attention()
    if villain.first_appearance < 1980:
        print(villain)
    aux_villain_queue.arrive(villain)

while aux_villain_queue.size() > 0:
    villain_queue.arrive(aux_villain_queue.attention())

print()
print("E")
#E
print("Superheroes que comienzan con 'Bl':")
for hero in list_superhero:
    if hero.name.startswith("Bl"):
        print(hero)
print()
print("Superheroes que comienzan con 'G':")
for hero in list_superhero:
    if hero.name.startswith("G"):
        print(hero)
print()
print("Superheroes que comienzan con 'My':")
for hero in list_superhero:
    if hero.name.startswith("My"):
        print(hero)
print()
print("Superheroes que comienzan con 'W':")
for hero in list_superhero:
    if hero.name.startswith("W"):
        print(hero)

print()
print("F")
#F
list_superhero.add_criterion("real_name", order_by_real_name)
list_superhero.sort_by_criterion("real_name")
list_superhero.show()
print()
print("G")
#G
list_superhero.add_criterion("first_appearance", order_by_first_appearance)
list_superhero.sort_by_criterion("first appearance")
list_superhero.show()
print()
print("H")
#H

print()
print("I")
#I

print()
print("J")
#J