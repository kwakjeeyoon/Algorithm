import numpy as np
arr = [2,6,8,14]
def LCM(arr):
    # 최소공배수 (Least commom multiple)
    for i in range(max(arr),np.prod(arr)+1):
        check = [i%a for a in arr]
        if check == [0]*len(arr):
            return i
def GCF(arr):
    # 최대공약수 (Greatest commom factor)
    for i in range(min(arr), 0, -1):
        check = [a%i for a in arr]
        if check == [0] * len(arr):
            return i
print('최소공배수: {}'.format(LCM(arr)))
print('최대공약수: {}'.format(GCF(arr)))