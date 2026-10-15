class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item not in "+-*/":
                stack.append(int(item))
            else:
                y = stack.pop()
                x = stack.pop()
                if item == "+":
                    stack.append(x+y)
                elif item == "-":
                    stack.append(x-y)
                elif item == "*":
                    stack.append( x * y)
                elif item == "/":
                    stack.append(int(x / y))
        return stack[0]