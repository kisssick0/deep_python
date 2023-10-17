import math


class Hook:
    def __init__(self):
        self.hook_num = 0

    def __get__(self, obj, objtype):
        return self.hook_num

    def __set__(self, obj, val):
        if not isinstance(val, (int, float)):
            raise TypeError("int or float required")
        if not val >= 1 or not val <= 12:
            raise ValueError("number great or equal than 1 or less or equal than 12 required")
        if not math.isclose(abs(int(val) - val), 0.0) and not math.isclose(abs(int(val) - val), 0.5):
            raise ValueError("number must be like 8 or 8.0 or 8.5")

        self.hook_num = val

    def __delete__(self, obj):
        del self.hook_num


class Materials:
    materials_list = ['cotton', 'polyester', 'silk', 'wool', 'acrylic', 'linen']

    def __init__(self):
        self.composition = 0

    def __get__(self, obj, objtype):
        return self.composition

    def __set__(self, obj, dct):
        if not isinstance(dct, dict) or not dct:
            raise TypeError("not empty dict required")

        count_percentages = 0
        for key, value in dct.items():
            if key not in self.materials_list:
                raise ValueError("valid materials: cotton, polyester, silk, wool, acrylic, linen")
            count_percentages += value
        if not math.isclose(count_percentages, 100):
            raise ValueError("the sum of the percentages of materials must be 100")

        self.composition = dct

    def __delete__(self, obj):
        del self.composition


class Clothes:
    clothes_pieces = ['sweater', 'top', 'vest', 'bag']

    def __init__(self):
        self.name = 0

    def __get__(self, obj, objtype):
        return self.name

    def __set__(self, obj, piece):
        if not isinstance(piece, str):
            raise TypeError("str required")

        if piece not in self.clothes_pieces:
            raise ValueError("clothes piece must be sweater, top, vest or bag")

        self.name = piece

    def __delete__(self, obj):
        del self.name


class CrochetClothes:
    hook = Hook()
    composition = Materials()
    piece = Clothes()

    def __init__(self, hook, composition, piece):
        self.hook = hook
        self.composition = composition
        self.piece = piece
