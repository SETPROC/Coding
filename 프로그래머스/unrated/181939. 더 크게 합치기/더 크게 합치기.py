def solution(a, b):
    if int(str(a)+str(b))>int(str(b)+str(a)):
        answer= str(a)+str(b)
    else:
        answer= str(b)+str(a)
    return int(answer)