def __init__(self, capacity):
    self.capacity = capacity
    self.slots = [None] * self.capacity


def __str__(self):
    return str(self.slots)


def __len__(self):
    count = 0
    for i in self.slots:
        if i != None:
            count += 1
    return count


def hash_function(self, key):
    i = key % self.capacity
    return i


def insert(self, key):
    slot = self.hash_function(key)
    orig = slot
    while True:
        if self.slots[slot] is None:
            self.slots[slot] = key
            return slot

        if self.slots[slot] == key:
            return -2

        slot = (slot + 1) % self.capacity
        if slot == orig:
            return -1


# https://stackoverflow.com/questions/33063260/python-myhashtable-class-search-method-with-linear-probing
