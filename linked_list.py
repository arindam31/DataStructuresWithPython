class node:
    def __init__(self, data=None):
        self.data = data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)

        #current node
        cur = self.head

        #Iterate over each node starting from head
        while cur.next != None:
            cur = cur.next

        cur.next = new_node


    def length(self):
        cur = self.head
        cnt = 0
        while cur.next != None:
            cur = cur.next
            cnt += 1

        return cnt

    def display(self):
        arr = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            arr.append(cur.data)
            
        return arr

    def get(self, index):
        if index >= self.length():
            print 'Error: Index out of bounds'
            return None
        cur = self.head
        for ind in range(index+1):
            if ind == index:
                cur = cur.next
                return cur.data
            else:
                cur = cur.next

    def erase(self, index):
        if index >= self.length():
            print 'Error: Index out of bounds'
            return None
        
        cur = self.head
        cur_idx = 0

       while True:
           last_node = cur
           cur_node=cur.next
           if cur_idx == index:
               last_node.next = cur_node.next
               return
            cur_idx+= 1
        

if __name__ == '__main__':
    l_obj = LinkedList()
    print l_obj.display()
    l_obj.append(1)
    l_obj.append(2)
    length = l_obj.length()
    print length
    
    l_obj.append(3)
    l_obj.append(4)
    print l_obj.display()

    print l_obj.get(0)
