class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search(self, item):
        try:
            index = len(self.items) - 1 - self.items[::-1].index(item)
            return index
        except ValueError:
            return -1

stack = Stack()

stack.push("Aku")
stack.push("Anak")
stack.push("Indonesia")

print("Next:", stack.peek())

stack.push("Raya")

print(stack.pop())

stack.push("!")

count = stack.search("Aku")
while count != -1 and count > 1:
    stack.pop()
    count -= 1

print(stack.peek())
print(stack.is_empty())

