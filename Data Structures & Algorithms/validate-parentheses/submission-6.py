class Solution:
    def isValid(self, s: str) -> bool:
        stack = [ ]
        closeToOpen = { "}" : "{" , ")" : "(" ,"]" : "["}
        for char in s: 
            if char in closeToOpen.values():
                stack.append(char)
            
            elif stack and stack[-1] == closeToOpen.get(char):
                stack.pop()
            else:
                return False

        
        return not(stack)