# 栈的实现
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        '''

        :return:判断栈是否为空
        '''
        return self.items == []

    def push(self, item):
        '''

        :param item:向栈内插入数据
        :return: 返回添加后的栈
        '''
        return self.items.append(item)

    def pop(self):
        '''
        :return:移除栈顶元素ß
        '''
        self.items.pop()

    def peek(self):
        '''
        :return:返回栈顶最后一个元素
        '''
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


