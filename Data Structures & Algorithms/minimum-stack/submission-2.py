class MinStack:

    def __init__(self):
        self.stack = []
        
        self.prevMins = [2**31]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.prevMins[-1]:
            self.prevMins.append(val) 


    def pop(self) -> None:
        if self.stack[-1] == self.prevMins[-1]:
            del self.prevMins[-1]
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prevMins[-1]
