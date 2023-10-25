from collections import deque


class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.deq = deque()
        self.dct = {}

    def get(self, key):
        if key in self.dct:
            self.deq.remove(key)
            self.deq.append(key)
            return self.dct[key]
        return None

    def set(self, key, value):
        if self.get(key) is not None:
            self.dct[key] = value
            return

        if len(self.deq) == self.limit:
            delete_key = self.deq.popleft()
            del self.dct[delete_key]
        self.deq.append(key)
        self.dct[key] = value
