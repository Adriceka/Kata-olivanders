from src.olivanders import Inventario, NormalItem


def test_simulacion_5_dias_item_normal():

    item = NormalItem("+5 Dexterity Vest", 10, 20)
    inventario = Inventario([item])

    for _ in range(5):
        inventario.update()

    assert item.sell_in == 5
    assert item.quality == 15


def test_item_normal_degrada_doble_despues_de_fecha():

    item = NormalItem("Normal", 1, 10)
    inventario = Inventario([item])

    for _ in range(2):
        inventario.update()

    assert item.quality == 7


def test_calidad_nunca_es_negativa():

    item = NormalItem("Normal", 0, 1)
    inventario = Inventario([item])

    for _ in range(5):
        inventario.update()

    assert item.quality == 0