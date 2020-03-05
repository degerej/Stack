from stack import LinkedList


class Stack:
    def __init__(self):
        self.my_list = LinkedList()

    def push(self, data):
        self.my_list.add_head(data)
