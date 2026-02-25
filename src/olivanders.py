class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


class Inventario:

    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:

            if item.sell_in > 0:
                decremento = 1
            else:
                decremento = 2

            if item.quality > 0:
                item.quality = max(0, item.quality - decremento)

            item.sell_in -= 1