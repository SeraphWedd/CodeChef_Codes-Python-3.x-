ANS = []

def to_RPN(expr):
    OP = '+ - / * ^ %'.split()
    a = []
    rpn = ''
    top = ''
    for char in expr:
        if char in OP or char == '(':
            a.append(char)
            top = a[-1]
        elif char == ')':
            while a[-1] != '(':
                rpn += a[-1]
                a = a[:-1]
            if a[-1] == '(':
                a = a[:-1]
        else:
            rpn += char

    for x in a:
        rpn += x
    ANS.append(rpn)
                
    
T = int(input())

for l in range(T):
    line = input()
    to_RPN(line)

for e in ANS:
    print(e)
    
