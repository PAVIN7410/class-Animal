class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")


### 2. Подклассы Bird, Mammal, и Reptile


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} chirps.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} roars.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} hisses.")


### 3. Полиморфизм


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Пример использования
animals = [
    Bird("Parrot", 2, "Medium"),
    Mammal("Lion", 5, "Golden"),
    Reptile("Snake", 3, "Smooth")
]

animal_sound(animals)


### 4. Класс Zoo с композицией


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} has been added to the zoo staff.")


### 5. Классы сотрудников


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")


### Пример использования


# Создаем зоопарк
zoo = Zoo()

# Добавляем животных
parrot = Bird("Parrot", 2, "Medium")
lion = Mammal("Lion", 5, "Golden")
snake = Reptile("Snake", 3, "Smooth")

zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

# Добавляем сотрудников
keeper = ZooKeeper("John")
vet = Veterinarian("Emily")

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Взаимодействие сотрудников с животными
keeper.feed_animal(lion)
vet.heal_animal(snake)






import pickle

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} has been added to the zoo staff.")

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
            print("Zoo state has been saved.")

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
            print("Zoo state has been loaded.")
            return zoo

# Пример использования

# Создаем зоопарк
zoo = Zoo()

# Добавляем животных
parrot = Bird("Parrot", 2, "Medium")
lion = Mammal("Lion", 5, "Golden")
snake = Reptile("Snake", 3, "Smooth")

zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

# Добавляем сотрудников
keeper = ZooKeeper("John")
vet = Veterinarian("Emily")

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Сохраняем состояние зоопарка
zoo.save('zoo_state.pkl')

# Загрузка состояния зоопарка
loaded_zoo = Zoo.load('zoo_state.pkl')

# Проверка загруженного состояния
for animal in loaded_zoo.animals:
    print(f"Animal: {animal.name}, Type: {type(animal).__name__}")

for staff in loaded_zoo.staff:
    print(f"Staff: {staff.name}, Type: {type(staff).__name__}")


