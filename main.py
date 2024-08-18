class Animal:
    def __init__(self,name):
        self.alive = True
        self.fed = False
        self.name = name


    def eat(self, food):
        self.food = food
        if food.edible:
            return f'{self.name},съел {food.name}'
        return f'{self.name} не стал есть {food.name}'

    def __str__(self):
        return f'животное : {self.name}'

class Mammal(Animal):
    def __init__(self,name,sound):
        super().__init__(name)
        self.sound = sound

    def make_sound (self):
        return f'{self.name} издал звук {self.sound}'



class Predator(Animal):
    def __init__(self,name):
        super().__init__(name)


    def hunt (self):
        return f'{self.name} вышел на охоту '

class Plant:
    def __init__(self,name):
        self.edible = False
        self.name = name



class Fruit(Plant):
    def __init__(self,name):
        super().__init__(name)





class Flower(Plant):
    def __init__(self,name):
        super().__init__(name)



if __name__ == '__main__': # почему выводится ссылка а не сам обьект?
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико','выхлопных газов')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    print(a1.eat(p1))
    print(a2.eat(p2),a2.make_sound())
    print(a1.alive)
    print(a2.fed)