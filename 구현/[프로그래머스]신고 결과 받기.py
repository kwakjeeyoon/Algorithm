from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    bad = defaultdict(int)
    good = defaultdict(int)
    for command in set(report):
        start, end = command.split()
        bad[end] += 1
    for command in set(report):
        start, end = command.split()
        if bad[end] >= k:
            good[start] += 1
    for id_num in id_list:
        answer.append(good[id_num])
    return answer

# 문제풀이
# 문제의 주요한 제한사항은 아래 두가지이다.
# 1. 2번 이상 신고당한 사람을 산고한 사람에게 메일은 보낸다
# 2. 한 유저가 2번 이상 한 유저를 신고할 수 없다. -> 이 조건은 set()으로 중복을 제거하면 되는 간단한 아이디어 였다.
# 1번 제한사항을 충족하기 위해서는
# 먼저 신고당한 사람이 몇번 신고당했는지 알려주는 딕셔너리(1)와
# 2번 이상 신고당한 사람을 신고한 사람에게 1씩 더해주는 딕셔너리(2)
# 총 2개의 딕셔너리가 필요하다.
