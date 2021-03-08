class HashRecord:
    def __init__(self, key, data):
        self.key = key
        self.value = data
        self.nxt = None


class HashTable:
    def __init__(self):
        self.table_size = 10
        self.current_size = 0
        self.table = [None] * self.table_size
        self.target_load_factor = 1.5

    def get_size(self):
        return self.current_size

    def is_empty(self):
        return int(self.get_size()) == 0

    def get_index(self, hash_value, table_size):
        return hash_value % table_size

    @staticmethod
    def get_hash(string):
        if not string:
            return 0

        hash_value = 0
        for ii in range(len(string)):
            hash_value += ord(string[ii])

        return hash_value

    def insert(self, key, value):
        hash_value = get_hash(key)
        table_index = self.get_index(hash_value, self.table_size)
        if self.table[table_index] is None:
            self.table[table_index] = HashRecord(key, value)
            print(key, "-", value, "inserted at index:", table_index)
            self.current_size += 1
        else:
            item = self.table[table_index]
            while item is not None:
                if item.key == key:
                    item.value = value
                    break
                elif item.nxt is None:
                    item.nxt = HashRecord(key, value)
                    print(key, "-", value, "inserted at index:", table_index)
                    self.current_size += 1
                    break
                item = item.nxt

        load_factor = float(self.current_size) / float(self.table_size)
        if load_factor >= self.target_load_factor:
            self.resize()

    def resize(self):
        new_table_size = self.table_size * 2
        new_table = [None] * new_table_size
        for i in range(0, len(self.table)):
            item = self.table[i]
            while item is not None:
                new_hash = get_hash(item.key)
                new_index = get_index(new_hash, new_table_size)

                if new_table[new_index] is None:
                    new_table[new_index] = HashRecord(item.key, item.value)
                else:
                    node = new_table[new_index]
                    while node is not None:
                        if node.key is item.key:
                            node.value = item.value
                            node = None
                        elif node.nxt is None:
                            node.nxt = HashRecord(item.key, item.value)
                            node = None
                        else:
                            node = node.nxt
                head = head.nxt
        self.table = new_table
        self.table_size = new_table_size