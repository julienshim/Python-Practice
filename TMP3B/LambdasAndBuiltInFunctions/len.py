print(len('laksdjflasdf'))  # 'laksdjflasdf'.__len__()
print(len({'s': 10, 'j': 20}))


class Specialist:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        # return 50
        return self.__data.__len__() // 2


l1 = Specialist([1, 2, 3, 4])
l2 = Specialist([])
print(len(l1))
print(len(l2))
