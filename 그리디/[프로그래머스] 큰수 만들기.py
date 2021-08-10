def solution(number, K):
    stack = []
    for i, num in enumerate(number):
        while stack and stack[-1]<num and K>0:
            stack.pop()
            K-=1
        if K==0:
            stack += number[i:]
            break
        stack.append(num)
    if K>0:
        stack = number[:-K]
    answer = ''.join(stack)
    return answer

number = "4177252841"
K = 4
print(solution(number, K))