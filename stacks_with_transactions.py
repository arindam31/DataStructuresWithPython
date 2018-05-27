# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class Solution(object):
    def __init__(self):
        self.items = []
        self.process_in_motion = False
        self.instructions = []

    def push(self, value):
        self.items.append(value)
        if self.process_in_motion:
                self.instructions.append(['push', value])


    def top(self):
        if self.items:
            return self.items[-1]
        else:
            return 0

    def pop(self):
        
        if self.items:
            popped = self.items.pop()
            if self.process_in_motion:
                self.instructions.append(['pop', popped])

    def begin(self):
        self.process_in_motion = True
        
    def rollback(self):
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
