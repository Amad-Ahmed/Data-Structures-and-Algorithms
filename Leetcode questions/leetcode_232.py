class MyQueue:

    def __init__(self):
        stack_one = []
        stack_two = []

    def push(self, x: int) -> None:
        if len(self.stack_one) == 0 and len(self.stack_two) == 0:
            self.stack_one.append(x)
        elif len(self.stack_one) > 0:
            self.stack_one.append(x)
        elif len(self.stack_two):
            self.stack_two.append(x)

    def pop(self) -> int:

        pass

    def peek(self) -> int:
        if len(self.stack_one > 0):
            while len(self.stack_one) > 0:
                if len(self.stack_one) == 1:
                    temp = self.stack_one.pop()
                    self.stack_two.append(temp)
                    return temp
                self.stack_two.append(self.stack_one.pop())
        else:
            while len(self.stack_two) > 0:
                if len(self.stack_two) == 1:
                    temp = self.stack_two.pop()
                    self.stack_one.append(temp)
                    return temp
                self.stack_one.append(self.stack_two.pop())

    def empty(self) -> bool:
        pass
