import sys
from collections import deque


def NUM(stack, x):
    try:
        stack.append(x)
    except:
        stack.append("ERROR")
    return stack

def POP(stack):
    try:
        stack.pop()
    except:
        stack.append("ERROR")
    return stack

def INV(stack):
    try:
        stack[-1] = -1*stack[-1]
    except:
        stack.append("ERROR")
    return stack

def DUP(stack):
    try:
        stack.append(stack[-1])
    except:
        stack.append("ERROR")
    return stack

def SWP(stack):
    try:
        a = stack.pop()
        b = stack.pop()
        stack.append(a)
        stack.append(b)
    except:
        stack.append("ERROR")
    return stack

def ADD(stack):
    try:
        a = stack.pop()
        b = stack.pop()
        if abs(a+b)>(10**9):
            stack.append("ERROR")
        else:
            stack.append(a+b)

    except:
        stack.append("ERROR")
    return stack

def SUB(stack):
    try:
        a = stack.pop()
        b = stack.pop()
        if abs(b-a)>(10**9):
            stack.append("ERROR")
        else:
            stack.append(b-a)
    except:
        stack.append("ERROR")
    return stack

def MUL(stack):
    try:
        a = stack.pop()
        b = stack.pop()
        if abs(a*b)>(10**9):
            stack.append("ERROR")
        else:
            stack.append(a * b)

    except:
        stack.append("ERROR")
    return stack

def DIV(stack):
    try:
        a = stack.pop()
        b = stack.pop()
        if a*b<0:
            stack.append(-1*(abs(b)//abs(a)))
        else:
            stack.append(abs(b) // abs(a))
    except:
        stack.append("ERROR")
    return stack

def MOD(stack):
    try:
        a = stack.pop()
        b = stack.pop()
        if b<0:
            stack.append(-1*(abs(b)%abs(a)))
        else:
            stack.append(abs(b) % abs(a))
    except:
        stack.append("ERROR")
    return stack

if __name__=="__main__":
    sys.stdin = open('../input.txt', 'r')
    program = []
    while True:
        operation = sys.stdin.readline().split()


        # case 0 : blank -> get next program
        if operation == []:
            program = []
            print("")
            continue

        # if operation is 'quit' stop program
        elif operation[0] == 'QUIT':
            break

        # case 1 : number -> get print value
        elif operation[0].isdigit():
            for _ in range(int(operation[0])):
                input_num = int(sys.stdin.readline())
                cur_stack = deque([input_num])
                for oper in program :
                    if cur_stack and cur_stack[-1] == "ERROR":
                        break

                    if oper[0]=='NUM':
                        cur_stack = NUM(cur_stack, int(oper[1]))
                    elif oper[0]=='POP':
                        cur_stack = POP(cur_stack)
                    elif oper[0]=='INV':
                        cur_stack = INV(cur_stack)
                    elif oper[0]=='DUP':
                        cur_stack = DUP(cur_stack)
                    elif oper[0]=='SWP':
                        cur_stack = SWP(cur_stack)
                    elif oper[0]=='ADD':
                        cur_stack = ADD(cur_stack)
                    elif oper[0]=='SUB':
                        cur_stack = SUB(cur_stack)
                    elif oper[0]=='MUL':
                        cur_stack = MUL(cur_stack)
                    elif oper[0]=='DIV':
                        cur_stack = DIV(cur_stack)
                    elif oper[0]=='MOD':
                        cur_stack = MOD(cur_stack)
                    else:
                        if (len(cur_stack)!=1):
                            cur_stack.append('ERROR')

                print(cur_stack[-1])



        else :
            program.append(operation)

