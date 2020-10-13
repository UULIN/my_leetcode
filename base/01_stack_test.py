from base.stack import Stack

# parChecker检查括号是否匹配
def parChecker(symbolString):
    s = Stack()
    index = 0
    balanced = True
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(parChecker('((('))
    print(parChecker('(())'))