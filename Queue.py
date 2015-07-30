__author__ = "Burkay Genc"

class QueueNode:
    def __init__(self):
        self.next = None
        self.value = None

    def __init__(self, val):
        self.next = None
        self.value = val

    def setNext(self, nextNode):
        self.next = nextNode

    def getNext(self):
        return self.next

    def getVal(self):
        return self.value


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, val):
        if self.head is None:
            self.head = QueueNode(val)
        else:
            node = self.head
            while node.getNext() is not None:
                node = node.getNext()
            node.setNext(QueueNode(val))

    def dequeue(self):
        if self.head is None:
            return None
        oldHead = self.head
        self.head = self.head.getNext()
        oldHead.setNext(None)
        return oldHead.getVal()

    def printQueue(self):
        node = self.head
        while node is not None:
            print node.getVal(),
            node = node.getNext()
        print ""

myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue("Burkay")
myQueue.enqueue(2.3)
myQueue.printQueue()
myQueue.enqueue(myQueue.dequeue())
myQueue.printQueue()