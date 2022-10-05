class CustomList(list):
    def __add__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only add list or CustomList to CustomList")

        new_lst = []
        max_len = max(len(self), len(lst))

        for i in range(max_len):
            if i >= len(self):
                new_lst.append(lst[i])
            elif i >= len(lst):
                new_lst.append(self[i])
            else:
                new_lst.append(self[i] + lst[i])

        return CustomList(new_lst)

    def __radd__(self, lst):
        return self + lst

    def __sub__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only sub list or CustomList to CustomList")

        new_lst = []
        max_len = max(len(self), len(lst))

        for i in range(max_len):
            if i >= len(self):
                new_lst.append(-lst[i])
            elif i >= len(lst):
                new_lst.append(self[i])
            else:
                new_lst.append(self[i] - lst[i])

        return CustomList(new_lst)

    def __rsub__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only sub list or CustomList to CustomList")

        new_lst = []
        max_len = max(len(self), len(lst))

        for i in range(max_len):
            if i >= len(self):
                new_lst.append(lst[i])
            elif i >= len(lst):
                new_lst.append(-self[i])
            else:
                new_lst.append(lst[i] - self[i])

        return CustomList(new_lst)

    def __lt__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only compare CustomList with CustomList")

        return sum(self) < sum(lst)

    def __gt__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only compare CustomList with CustomList")

        return sum(self) > sum(lst)

    def __le__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only compare CustomList with CustomList")

        return sum(self) <= sum(lst)

    def __ge__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only compare CustomList with CustomList")

        return sum(self) >= sum(lst)

    def __eq__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only compare CustomList with CustomList")

        return sum(self) == sum(lst)

    def __ne__(self, lst):
        if not isinstance(lst, list) and not isinstance(lst, CustomList):
            raise TypeError("can only compare CustomList with CustomList")

        return sum(self) != sum(lst)

    def __str__(self):
        return f'CustomList({list(self)})\nsum={sum(self)}'
