# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def eat(self):
        print(f"{self.name} is eating.")

# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says Chirp!")

# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says Roar!")

# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says Hiss!")

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} has joined the zoo staff.")

# Базовый класс Staff
class Staff:
    def __init__(self, name):
        self.name = name

# Подкласс ZooKeeper
class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

# Подкласс Veterinarian
class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

# Демонстрация работы программы
zoo = Zoo()

# Создание и добавление животных
parrot = Bird("Parrot", 2)
tiger = Mammal("Tiger", 5)
snake = Reptile("Snake", 3)

zoo.add_animal(parrot)
zoo.add_animal(tiger)
zoo.add_animal(snake)

# Создание и добавление сотрудников
keeper = ZooKeeper("John")
vet = Veterinarian("Alice")

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Вызов метода make_sound для каждого животного
print("\nAnimal sounds:")
animal_sound(zoo.animals)

# Использование методов сотрудников
keeper.feed_animal(tiger)
vet.heal_animal(snake)