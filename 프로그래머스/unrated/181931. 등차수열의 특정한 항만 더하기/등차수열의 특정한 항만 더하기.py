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
            