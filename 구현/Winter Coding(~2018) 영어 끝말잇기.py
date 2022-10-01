import math
def solution(n, words):
    answer = [0,0]
    done_i, done_w = [], []
    num = 0
    b_word = words[0][0]
    while words:
        num += 1
        if num%n != 0:
            idx = num%n
        else:
            idx = n
        word_n = words.pop(0)
        if len(word_n) == 1 or word_n[0] != b_word[-1] or word_n in done_w:
            print(num, n)
            return [idx, math.ceil(num/n)]
        else:
            done_i.append(idx)
            done_w.append(word_n)
            b_word = word_n
    return answer