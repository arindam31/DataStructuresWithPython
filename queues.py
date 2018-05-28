# FIFO

class Queue:
    """
    My list will be: latest items at the front i.e index 0. Oldest at the back i.e at index -1
    """

    def __init__(self):
        self.items = []

    def push(self, value):
        # Add item at the head i.e index 0 of the list
        self.items.insert(0, value)

    def pop(self):
        # Remove the oldest item i.e which was inserted first
        if self.items:
            popped = self.items.pop()
            return popped

    def empty(self):
        self.items = []

    def view(self):
        #
        for i in range(len(self.items)-1, -1, -1):
            print self.items[i]

que = Queue()

#Add items
que.push('a')
que.push('b')
que.push('c')
que.push('d')

#View the queue
print "The Queue Now"
que.view()

#Remove 2 items
que.pop()
que.pop()

#View the queue

print "The Queue after 2 pop operations"
que.view()

assert(['d', 'c'] == que.items)

print "The Queue after new push operation"
que.push('x')
que.view()
