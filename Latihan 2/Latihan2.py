class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def queue_example(self):
        queue = Queue()
        queue.enqueue("Java")
        queue.enqueue("DotNet")
        queue.enqueue("PHP")
        queue.enqueue("HTML")
        print("remove: ", queue.dequeue())
        print("element: ", queue.peek())
        print("poll: ", queue.dequeue())
        print("peek: ", queue.peek())

if __name__ == '__main__':
    q = Queue()
    q.queue_example()
