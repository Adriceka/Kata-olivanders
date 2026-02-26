class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self._quality = quality  

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = max(0, min(50, value))


class Inventario:
    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:
            item.update()

class NormalItem(Item):

    def update(self):
        decremento = 1 if self.sell_in > 0 else 2
        self.quality -= decremento
        self.sell_in -= 1


class AgedBrie(Item):

    def update(self):
        incremento = 1 if self.sell_in > 0 else 2
        self.quality += incremento
        self.sell_in -= 1

class Sulfuras(Item):

    def __init__(self, name, sell_in, quality=80):
        super().__init__(name, sell_in, 80)

    def update(self):
        pass


class Backstage(Item):

    def update(self):
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in > 5:
            self.quality += 2
        elif self.sell_in > 0:
            self.quality += 3
        else:
            self.quality = 0

        self.sell_in -= 1


class Conjured(Item):

    def update(self):
        decremento = 2 if self.sell_in > 0 else 4
        self.quality -= decremento
        self.sell_in -= 1