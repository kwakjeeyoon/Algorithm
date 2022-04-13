from collections import defaultdict
li = list(map(int, input().split(' ')))
dict = defaultdict(int)
for i in li:
    dict[i]+=1

def prize(dict):
    for key, item in dict.items():
        if item == 2: # 같은 눈 2개
            output = 1000 + key * 100
            return output
        elif item == 3: # 같은 눈 3개
            output = 10000 + key * 1000
            return output
        else:
            output = max(li) * 100
    return output
print(prize(dict))