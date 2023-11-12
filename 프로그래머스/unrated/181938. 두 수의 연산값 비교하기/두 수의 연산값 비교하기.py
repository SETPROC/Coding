def solution(a, b):
    temp = []
    temp.append(int(str(a)+str(b)))
    temp.append(2*a*b)
    return max(temp[0],temp[1])