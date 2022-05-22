class Calculator():

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
    '''
    生成后缀表达式
    '''
    def toSuffixExpression(self, expression):
        # 去除表达式中所有空格
        expression = expression.replace(' ', '')
        # 操作符栈
        operatorStack = []
        # 后缀表达式队列
        suffixQueue = []

        for element in expression:
            # 如果是数字则直接入表达式栈
            if element in self.operators:
                # 如果栈为空，操作符直接入操作符栈，或者为左括号，也直接入操作符栈
                if not operatorStack:
                    operatorStack.append(element)
                else:
                    # 如果目标元素是右括号，操作符栈顶出栈直接遇到左括号，且出栈的操作符除了括号入到表达式队列中
                    if element == ')':
                        for top in operatorStack[::-1]:
                            if top != '(':
                                suffixQueue.append(top)
                                operatorStack.pop()
                            else:
                                operatorStack.pop()
                                break
                    else:
                        for top in operatorStack[::-1]:
                            # 如果目标元素大于栈顶元素，则直接入栈，否则栈顶元素出栈，入到表达式队列中
                            # 左括号只有遇到右括号才出栈
                            if self.priority[top] >= self.priority[element] and top != '(':
                                suffixQueue.append(top)
                                operatorStack.pop()
                            else:
                                operatorStack.append(element)
                                break
                        # 可能操作符栈所有的元素优先级都大于等于目标操作符的优先级，这样的话操作符全部出栈了，
                        # 而目标操作符需要入栈操作
                        if not operatorStack:
                            operatorStack.append(element)
            else:
                suffixQueue.append(element)
        # 中缀表达式遍历结束，操作符栈仍有操作符，将操作符栈中的操作符入到表达式栈中
        for i in range(len(operatorStack)):
            suffixQueue.append(operatorStack.pop())
        return suffixQueue

if __name__ == '__main__':
    c = Calculator()
    expression = '3 + ( ( 9 - 5 ) * 2 - ( 4 + 4 ) / 2 ) * 3 - 5'
    suffixExpression = c.toSuffixExpression(expression)
    print(suffixExpression)
