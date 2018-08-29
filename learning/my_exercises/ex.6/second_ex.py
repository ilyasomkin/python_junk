class MyList:
    def __init__(self, data):
        self.data = []
        for i in data: self.data.append(i)

    def __add__(self, value):
        return MyList(self.data + value)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, offset):
        return self.data[offset]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item

    def append(self, value):
        return self.data.append(value)

    def sort(self):
        return self.data.sort()
