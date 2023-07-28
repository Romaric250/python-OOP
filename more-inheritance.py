class MyList:
    def __init__(self):
        self._li = []

    def append(self, item):
        self._li.append(item)
    def __getitem__(self, index):

        return self._li[index]

li = MyList()

li.append(1)
li.append(45)
li.append(676)
li.append(3)
li.append(2457)
#the magic method __getitem__
# allows us to use square bracket notations with our class
print(li[4])
