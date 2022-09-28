# 배운 스킬
# 1. ['C#','D#','F#','G#','A#'] 와 같이 2개의 문자열은 replace를 사용해서 소문자 ['c','d','f','g','a']로 치환
# 2. 문자열 slicing 할때 (전체 문자열 길이 - 부분 문자열 길이 + 1) 해줘야 되는거 까먹지 말기!!!
# 3. > import math >math.ceil(num1/num2) 적극 활용하기
# 4. 시간 계산 방법 통일하기!!! (hour-hour + min-min) 이런 식으로 하면 오류남
import math
def pound_key(m): # 1. replace 로 간단하게 해결 가능
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
def time_cal(start, end): # 4. hour-hour + min-min 으로 계산하지 말고 (start_m-end_m) 이렇게 계산!
    # min = 0
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    # if end_m>=start_m:
    #     min += end_m - start_m
    # else:
    #     min += 60 + end_m - start_m
    # min += (end_h-start_h)*60
    min = (end_h * 60 + end_m) - (start_h * 60 + start_m)
    return min
def solution1(m, musicinfos):
    # return None
    can = dict()
    heard = pound_key(m)
    # input 전처리
    for info in musicinfos:
        start, end, name, liric = info.split(',')
        total_min = time_cal(start, end)
        b_liric = pound_key(liric)
        b_liric *= math.ceil(total_min/len(b_liric)) # 3. math.ceil 적극 활용!
        a_liric = b_liric[:total_min]
        for idx in range(len(a_liric)-len(heard)+1): # 2. slicing 할때는 +1 !!!
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
