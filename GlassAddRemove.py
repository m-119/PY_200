class GlassAddRemove:
    cnt = 1

    def __init__(self, capacity: float = 200, occupied: float = 0):
        self.capacity_volume: float
        self.occupied_volume: float
        self.cnt = Glass.cnt

        if not isinstance(capacity, (int, float)):
            raise TypeError("Некоррктный тип capacity")
        if not isinstance(occupied, (int, float)):
            raise TypeError("Некоррктный тип occupied")

        if occupied > capacity or capacity < 0 or occupied < 0:
            raise ValueError("Некорректный объем")

        self.capacity_volume = capacity
        self.occupied_volume = occupied
        GlassAddRemove.cnt += 1

    def __del__(self):
        GlassAddRemove.cnt -= 1
        print(f"cnt: {Glass.cnt}")

    def __str__(self):
        return f"Glass str: {self.cnt}"

    def __repr__(self):
        return f"Glass repr: {self.cnt}"

    def add_water(self, value: float = 0):
        result = value + self.occupied_volume
        if result > self.occupied_volume or result < 0:
            return result
        else:
            self.occupied_volume = result
            return 0

    def del_water(self, value: float = 0):
        new_val = -value
        self.add_water(new_val)