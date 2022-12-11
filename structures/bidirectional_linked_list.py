class Elem:
    def __init__(self, value=None, prev_elem=None, next_elem=None):
        self.value = value
        self.next_elem = next_elem
        self.prev_elem = prev_elem

class LinkedList:
    def __init__(self, iterable_object=None):
        self.length = 0
        self.head = None
        self.tail = None

        if iterable_object:
            for value in iterable_object:
                self.append(value)

    def append(self, value):
        self.length += 1
        if self.tail is None:
            self.tail = self.head = Elem(value) # None <- Elem(value) -> None
        else:
            old_tail = self.tail
            self.tail = Elem(value, prev_elem=old_tail) # old_tail <- Elem(value) -> None
            old_tail.next_elem = self.tail # old_tail -> Elem(value)

    def insert(self, value):
        self.length += 1
        if self.head is None:
            self.tail = self.head = Elem(value) # None <- Elem(value) -> None
        else:
            old_head = self.head
            self.head = Elem(value, next_elem=old_head) # None <- Elem(value) -> old_head
            old_head.prev_elem = self.head # Elem(value) <- old_head

    def __iter__(self):
        return LinkedListIterator(self)

    def __str__(self):
        string = '['
        for i, elem in enumerate(self):
            string += str(elem)
            if i < self.length - 1:
                string += ', '
        string += ']'
        return string

    def __getitem__(self, number: int):
        if number >= self.length:
            raise IndexError(f'index {number} is out of linked list length')

        for i, elem_value in enumerate(self):
            if i == number:
                return elem_value

    def __len__(self):
        return self.length

class LinkedListIterator:
    def __init__(self, iterable_list: LinkedList):
        self.cur_elem = iterable_list.head

    def __next__(self):
        if self.cur_elem is None:
            raise StopIteration
        result = self.cur_elem.value
        self.cur_elem = self.cur_elem.next_elem
        return result


if __name__ == '__main__':

    linked_list = LinkedList([1, 2, 3])
    print(linked_list, len(linked_list)) # [1, 2, 3] 3

    linked_list.append(4)
    print(linked_list, len(linked_list)) # [1, 2, 3, 4] 4

    linked_list.insert(0)
    print(linked_list, len(linked_list)) # [0, 1, 2, 3, 4] 5

    print(linked_list[1], linked_list[4]) # 1 4