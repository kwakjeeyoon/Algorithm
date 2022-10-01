# LRU(Least Recently Used) 알고리즘
# 페이지 부재가 발생했을 경우, 가장 오랫동안 사용되지 않은 페이지를 제거하는 알고리즘
# 개념 : https://gingerkang.tistory.com/26
def solution(cacheSize, cities):
    answer = 0
    cities = [i.lower() for i in cities]
    cache = []
    for city in cities:
        # 적중 실패 (cache miss)
        if not city in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache.append(city)
                cache.pop(0)
        # 적중 성공 (cache hit)
        else:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
    return answer