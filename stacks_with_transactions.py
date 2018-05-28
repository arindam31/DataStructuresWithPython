
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

    def begin(self):
        # This is for beginning of a transaction.
        # We save the state of the database here
        self.transaction_in_progress = True
        self.backup = self.items
        
    def rollback(self):
        # This is to roll back all steps in transaction
        self.items = self.backup

    def commit(self):
        #If all goes well, lets all steps executed remain
        # (or execute if we are storing steps to be performed, not executing).
        pass
        


def test():
    # Define your tests here
    sol = Stack()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"
