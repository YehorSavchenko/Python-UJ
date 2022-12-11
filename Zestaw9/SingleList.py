class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def __iter__(self):  # wykorzystanie funkcji generatora
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        node = self.head
        list_string = ""
        while node:
            list_string += f'{node.data} '
            node = node.next
        return list_string

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def search(self, data):  # klasy O(n) # Zwraca łącze do węzła o podanym kluczu lub None.
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def find_min(self):  # klasy O(n)  # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        node = self.head
        minimum = node
        while node:
            if node.data < minimum.data:
                minimum = node
            node = node.next
        return minimum

    def find_max(self):  # klasy O(n)  # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        if self.is_empty():
            return None
        node = self.head
        maximum = node
        while node:
            if node.data > maximum.data:
                maximum = node
            node = node.next
        return maximum

    def reverse(self):  # klasy O(n) # Odwracanie kolejności węzłów na liście.
        before = None
        after = self.head
        while after:
            node = after.next
            after.next = before
            before = after
            after = node
        self.tail = self.head
        self.head = before


# Zastosowanie.
alist = SingleList()
alist.insert_head(Node(11))  # [11]
alist.insert_head(Node(22))  # [22, 11]
alist.insert_tail(Node(33))  # [22, 11, 33]

# for item in alist:  # kolejność 22, 11, 33
#     print(f'{item}')
print(f'SingleList: {alist}')

print(f'Search: {alist.search(33)}')
print(f'Min: {alist.find_min().data}')
print(f'Max: {alist.find_max().data}')
alist.reverse()

print(f'Reverse head: {alist.head.data}')
print(f'Reverse tail: {alist.tail.data}')

print("length {}".format(alist.length))  # odczyt atrybutu
print("length {}".format(alist.count()))  # wykorzystujemy interfejs

for item in alist:  # kolejność 22, 11, 33
    print(f'{item}')

while not alist.is_empty():  # kolejność 22, 11, 33
    print("remove head {}".format(alist.remove_head()))
