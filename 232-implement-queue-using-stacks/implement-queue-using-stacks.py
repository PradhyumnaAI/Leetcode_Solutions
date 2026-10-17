class MyQueue:

    def __init__(self):
        self.s1 = []  # Input stack
        self.s2 = []  # Output stack

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()  # Ensures s2 has the front elements ready
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            # Transfer all elements from s1 to s2 to reverse order
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2