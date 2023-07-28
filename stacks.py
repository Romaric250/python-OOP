class Stacks:
    def __int__(self):
        self._li  = []

    def push(self, item):
        self._li.append(item)
    def pop(self):
        return self._li.pop()
    def peeek(self):
        return self._li[-1]
    def __len__(self):
        return len(self._li)
    def __str__(self):

        return "i am a stack object"

l = Stacks()

l.push(4)
l.push(3)
l.push(34)
l.push(23)

print(l.pop)