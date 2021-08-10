def solution(routes):
    routes.sort(key=lambda x:x[0])
    answer = 0
    queue = [routes.pop(0)]
    while queue:
        queue.sort(key=lambda x:x[1])
        if routes:
            new = routes.pop(0)
            if new[0] <= queue[0][1]:
                queue.append(new)
            else:
                answer += 1
                queue = [new]
            print(queue, routes)
        else:
            answer+=1
            break
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))