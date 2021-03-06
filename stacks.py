
class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def top(self):
        if self.items:
            return self.items[-1]
        else:
            return 0

    def pop(self):
        if self.items:
            popped = self.items.pop()
            return int(popped)
        else:
            return 0

def test():
    # Define your tests here
    sol = Stack()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"
