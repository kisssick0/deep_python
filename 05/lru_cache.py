class ListNode:
    def __init__(self, key, value, next_node=None, prev_node=None):
        self.key = key
        self.value = value
        self.next = next_node
        self.prev = prev_node


class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.dct = {}
        self.head = None
        self.tail = None
        self.list = ListNode

    def get(self, key):
        if key not in self.dct:
            return None

        if self.dct[key] is not self.tail:
            self.remove_at(key)
            new_node = self.list(key, self.dct[key].value)
            self.dct[key] = new_node
            self.insert_right(new_node)
        return self.dct[key].value

    def set(self, key, value):
        new_node = self.list(key, value)
        if key in self.dct:
            if self.dct[key] is not self.tail:
                self.remove_at(key)
                self.insert_right(new_node)
                self.dct[key] = new_node
            else:
                self.tail.value = value
        elif len(self.dct) < self.limit:
            if len(self.dct) == 0:
                self.head = self.tail = new_node
            else:
                self.insert_right(new_node)
            self.dct[key] = new_node
        else:
            if self.head is self.tail:
                self.dct.pop(self.head.key)
                self.head.value = value
                self.head.key = key
                self.dct[key] = self.head
            else:
                prev_head_key = self.remove_left()
                self.dct.pop(prev_head_key)
                self.insert_right(new_node)
                self.dct[key] = new_node

    def insert_right(self, new_node):
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove_left(self):
        prev_head_key = self.head.key
        self.head = self.head.next
        self.head.prev = None
        return prev_head_key

    def remove_at(self, key):
        if self.dct[key] is self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            curr_node = self.dct[key]
            curr_node.next.prev = curr_node.prev
            curr_node.prev.next = curr_node.next
