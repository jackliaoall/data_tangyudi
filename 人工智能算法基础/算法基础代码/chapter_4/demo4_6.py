class Caculate():
    def __init__(self):
        # 操作符集合
        self.operators = ['+', '-', '*', '/', '(', ')']
        # 操作符优先级
        self.priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '(': 3,
            ')': 3
        }

    def caculate(self, expression):
        # 使用列表作为栈来计算
        stack = []
        # 遍历后缀表达式
        for element in expression:
            # 如果为数字直接入栈
            # 遇到操作符，将栈顶的两个元素出栈
            if element not in self.operators:
                stack.append(element)
            else:
                # 操作数
                number1 = stack.pop()
                # 被操作数
                number2 = stack.pop()
                # 结果 =  被操作数 操作符 操作数 （例：2 - 1）
                result = self.operate(number1, number2, element)
                # 计算结果入栈
                stack.append(result)
        return stack[0]

    '''
    计算结果
    number1: 操作数
    number2: 被操作数
    operator: 操作符
    '''

    def operate(self, number1, number2, operator):

        number1 = int(number1)
        number2 = int(number2)

        if operator == '+':
            return number2 + number1
        if operator == '-':
            return number2 - number1
        if operator == '*':
            return number2 * number1
        if operator == '/':
            return number2 / number1


if __name__ == '__main__':
    src = ['3', '4', '+', '2', '*']
    c = Caculate()
    result = c.caculate(src)
    print(result)
