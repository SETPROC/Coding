def solution(ineq, eq, n, m):
    x = [">=","<=",">!","<!"]
    if ineq+eq == x[0]:
        return int(n >= m)
    elif ineq+eq == x[1]:
        return int(n <= m)
    elif ineq+eq == x[2]:
        return int(n>m)
    else:
        return int(n<m)