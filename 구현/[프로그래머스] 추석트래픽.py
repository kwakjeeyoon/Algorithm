def solution(lines):
    answer = 0
    li = []
    for line in lines:
        start_end = []
        date, end, during = line.split(' ')
        h, m, s = map(float, end.split(":"))
        end = h*60*60 + m*60 + s
        start = end - float(during[:-1]) + 0.001
        li.append((start, end))
    count_li = []
    for n in range(len(lines)):
        s_li = li.pop(0)
        for s_start in s_li:
            count = 1
            s_end = round(s_start + 1 - 0.001, 3)
            for i, (c_start, c_end) in enumerate(li):
                if c_start <= s_start and s_end <= c_end:
                    count += 1
                elif c_start >= s_start  and s_end >= c_end:
                    count += 1
                elif c_start <= s_start <= c_end and s_start <= c_end:
                    count += 1
                elif c_start <= s_end <= c_end and s_start <= c_start:
                    count += 1
            count_li.append(count)
    return max(count_li)

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(lines))