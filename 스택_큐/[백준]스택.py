import sys
input = sys.stdin.readline

stack = []
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'size':
        print(len(stack))
        continue
    if stack:
        if command[0] == 'pop':
            output = stack.pop()
            print(output)
        elif command[0] == 'empty':
            print(0)
        elif command[0] == 'top':
            print(stack[-1])
    else:
        if command[0] == 'pop':
            print(-1)
        elif command[0] == 'empty':
            print(1)
        elif command[0] == 'top':
            print(-1)
