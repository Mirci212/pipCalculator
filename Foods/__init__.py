class Food:
    _name: str
    _weight: float

    @property
    def Weight(self):
        return self._weight

    @Weight.setter
    def Weight(self, value: float):
        if value < 0:
            return
        self._weight = value

    @property
    def Name(self):
        return self._name

    def __init__(self, Name: str, Weight: float):
        self._name = Name
        self.Weight = Weight

    def __str__(self):
        return f'{self.Name} weights {self.Weight}kg'


class Foodlist:
    _foodList: list[Food]

    def __init__(self):
        self._foodList = []

    def addFood(self, food: Food):
        self._foodList.append(food)

    def __str__(self):
        s = ""
        for food in self._foodList:
            s += str(food) + "\n"
        return s
