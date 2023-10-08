class CustomList(list):
    def __add__(self, other):
        lst1 = self.copy()
        lst2 = other.copy()

        while len(lst1) != len(lst2):
            if len(lst1) < len(lst2):
                lst1.append(0)
            else:
                lst2.append(0)

        clst = CustomList()
        for i, elem in enumerate(lst1):
            clst.append(elem + lst2[i])
        return clst

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        lst1 = self.copy()
        lst2 = other.copy()

        while len(lst1) != len(lst2):
            if len(lst1) < len(lst2):
                lst1.append(0)
            else:
                lst2.append(0)

        clst = CustomList()
        for i, elem in enumerate(lst1):
            clst.append(elem - lst2[i])
        return clst

    def __rsub__(self, other):
        return CustomList.__sub__(other, self)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f'{list(self)} sum={sum(self)}'
