class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            else:
                num2=int(stack.pop())
                num1=int(stack.pop())
                if i == "+":
                    result=num1+num2
                    stack.append(result)
                elif i=="-":
                    result=num1-num2
                    stack.append(result)
                elif i=="*":
                    result=num1*num2
                    stack.append(result)
                elif i=="/":
                    result = int(num1 / num2)
                    stack.append(result)

        return stack[-1]