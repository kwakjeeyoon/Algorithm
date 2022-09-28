def pound_key(m):
    remem = list()
    m = list(m)
    while m:
        now = m.pop()
        if now.isalpha():
            remem.insert(0, now)
        else:
            now_plus = m.pop()
            remem.insert(0, now_plus+now)
    return remem
def time_cal(start, end):
    min = 0
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    if end_m>=start_m:
        min += end_m - start_m
    else:
        min += 60 + end_m - start_m
    min += (end_h-start_h)*60
    return min
def solution(m, musicinfos):
    # return None
    can = dict()
    heard = pound_key(m)
    # input 전처리
    for info in musicinfos:
        start, end, name, liric = info.split(',')
        total_min = time_cal(start, end)
        print(total_min)
        b_liric = pound_key(liric)
        b_liric = b_liric*(total_min//len(b_liric)+1)
        a_liric = b_liric[:total_min]
        for idx in range(len(a_liric)-len(heard)):
            compare = ''.join(a_liric[idx:idx+len(heard)])
            if compare == m:
                can[name]=total_min
                break
    if can:
        can_sort = sorted(can.items(), key=lambda x:x[1], reverse=True)
        re_can = [name for name, min in can_sort if min==can_sort[0][1]]
        print(can, can_sort)
        print(re_can)
        for key, value in can.items():
            if key in re_can:
                return key
    else:
        return "(None)"
