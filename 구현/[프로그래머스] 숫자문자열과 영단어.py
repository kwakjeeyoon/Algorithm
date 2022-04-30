def solution(s):
    answer = ''
    dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
            'six':6, 'seven':7, 'eight':8, 'nine':9}
    word = ''
    s = list(s)
    while s:
        now = s.pop(0)
        if now.isnumeric():
            answer += now
        else:
            word += now
        try:
            answer += str(dict[word])
            word = ''
        except:
            pass
    return int(answer)

# 문제풀이
# 1. 먼저 각 영단어가 의미하는 숫자가 담긴 딕셔너리를 생성한다
# 2. 주어진 문자열을 list로 하나씩 쪼개고
# 3. for 문으로 문자 하나씩 보면서 숫자면 숫자 그래로 answer에 더하고 문자면 word 변수에 하나씩 더하여
#    문자가 다 완성되었을 때 try를 적용하여 answer에 해당하는 숫자를 넣고 word 변수를 초기화한다.
# 배운점 : txt.isnumeric() 은 숫자를 True/False로 판별하는 명령어