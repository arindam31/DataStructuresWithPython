
class Solution(object):
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
        # This is for beginning of a transaction
        self.process_in_motion = True
        
    def rollback(self):
        # This is to roll back all steps in transaction
        if self.process_in_motion:
            for instr in self.instructions[::-1]:
                if instr[0] == 'push':
                    self.items.remove(instr[1])
                else:
                    self.items.append(instr[1])
            return True
        else:
            return False

    def commit(self):
        #If all goes well, lets all steps executed remain (or execute if we are storing steps to be performed, not executing).
        for instr in self.instructions[::-1]:
            if instr[0] == 'push':
                self.items.remove(instr[1])
            else:
                self.items.append(instr[1])
        
        self.process_in_motion = False
        self.instructions = []


def test():
    # Define your tests here
    sol = Solution()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"
