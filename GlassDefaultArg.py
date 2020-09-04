class GlassDefaultArg:
    def __init__(self, occupied: float = 0):
        self.occupied_volume: float

        if not isinstance(occupied, (int, float)):
            raise TypeError("Некоррктный тип occupied")
        if occupied < 0:
            raise ValueError("Некорректный объем occupied")

        self.occupied_volume = occupied