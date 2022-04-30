from collections import defaultdict
def solution(N, stages):
    now = len(stages)
    answer_score = {}
    for key in range(1, N+1):
        if now:
            num = stages.count(key)
            answer_score[key] = num/now
            now -= num
        else:
            answer_score[key]=0
    answer = [k for k,v in sorted(answer_score.items(), key = lambda x:x[1], reverse=True)]
    return answer

# 문제풀이
# 각 스테이지의 실패율을 구하기 위해 stages에서 해당 스테이지의 개수 / 사용자 중 해당 스테이지에 도달한 사람
# 을 구해야 되는데 분모는 for 문을 1 씩 증가하면서 분자의 개수를 전체 사용자에서 빼는식으로 계산하면 됨

# else 문을 안넣어줘서 몇개의 테스트 케이스가 틀렸다.
# 해당 스테이지 이후 통과한 사람이 없어도 0으로 실패율이 들어갈 수 있게 해줘야 됨.