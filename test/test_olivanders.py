from src.olivanders import Inventario, Item

def test_un_item_normal_se_actualiza_correctamente():
    inventario = Inventario([
        Item("Normal", sell_in=10, quality=20)
    ])

    inventario.update()

    item = inventario.items[0]
    assert item.sell_in == 9
    assert item.quality == 19