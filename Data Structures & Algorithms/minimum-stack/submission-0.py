class MinStack:

    # Brute force approach using only stack and Iterating through all over the stack

    # def __init__(self):
        
    #     self.stack = []
     

    # def push(self, val: int) -> None:

    #     self.stack.append(val)
    

    # def pop(self) -> None:
        
    #     self.stack.pop()


    # def top(self) -> int:
        
    #     return self.stack[-1]

    # def getMin(self) -> int:

    #     min = self.stack[0]

    #     for value in self.stack:

    #         if value < min:
    #             min = value

    #     return min


    # optimal approach using two stacks

    def __init__(self):
        
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:

        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val > self.min_stack[-1]:

                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(val)

    def pop(self) -> None:
        
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        
        return self.stack[-1]

    def getMin(self) -> int:

        return self.min_stack[-1]

        
        
