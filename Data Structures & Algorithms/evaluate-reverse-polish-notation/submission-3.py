class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curStack = []
        for i in range(len(tokens)):
            if(tokens[i] == "*") and len(curStack) > 1:
                curStack.append(int(curStack.pop(-2)) * int(curStack.pop()))
            elif(tokens[i] == "/") and len(curStack) > 1:
                curStack.append(int((curStack.pop(-2)) / int(curStack.pop())))
            elif(tokens[i] == "-") and len(curStack) > 1:
                curStack.append(int(curStack.pop(-2)) - int(curStack.pop()))
            elif(tokens[i] == "+") and len(curStack) > 1:
                
                curStack.append(int(curStack.pop(-2)) + int(curStack.pop()))
            else: 
                curStack.append(int(tokens[i]))
        return curStack[0]
