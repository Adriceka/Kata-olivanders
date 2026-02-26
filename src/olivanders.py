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