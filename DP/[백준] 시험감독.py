N = int(input())
student_li = list(map(int, input().split()))
main, sub = map(int, input().split())
answer = 0
for stu in student_li:
    answer += 1
    if stu-main >0:
        if (stu-main)/sub == int((stu-main)/sub):
            answer += (stu-main)//sub
        else:
            answer += (stu - main) // sub +1

print(answer)