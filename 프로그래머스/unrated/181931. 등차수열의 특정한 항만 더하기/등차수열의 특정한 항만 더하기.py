def solution(a, d, included):
    s = 0
    total = 0
    for idx, data in enumerate(included):
        if idx == 0:
            s = a
            if data:
                total += s
        else:
            s += d
            if data:
                total += s
    return total

"""
다른 사람 코드 i=0이라면 공차는 더해지지 않는다는 점을 활용해야 한다.
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * int(included[i])
    return answer
"""
            