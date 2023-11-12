def solution(n):
    if n%2:
        return sum(list(range(1,n+1,2)))
    else:
        return sum(map(lambda x: x*x,list(range(2,n+1,2))))