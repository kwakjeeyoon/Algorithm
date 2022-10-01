def solution(s):
    check = 1
    remain = []
    s=list(s)
    b_alpha = ''
    while check == 1:
        check = 0
        for i in s:
            if i==b_alpha:
                check = 1
                remain.pop()
                if remain:
                    b_alpha = remain[-1]
                else:
                    b_alpha = ''
            else:
                remain.append(i)
                b_alpha = i
        s = ''.join(remain)
        remain = []
        b_alpha = ''
    print(s)
    if s:
        return 0
    else:
        return 1