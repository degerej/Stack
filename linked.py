from stack import LinkedList


class Stack:
    def __init__(self):
        self.my_list = LinkedList()

    def push_head(self, data):
        self.my_list.add_head(data)

    def push_end(self, data):
        self.my_list.add_end(data)

    def pop_head(self):
        self.my_list.remove_head()

    def pop_end(self):
        self.my_list.remove_end()
