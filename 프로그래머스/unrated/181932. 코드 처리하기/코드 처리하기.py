def solution(code):
    mode = 0
    answer = ''
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1':
                if not(i%2):
                    answer += code[i]
            else:
                 mode = 1   
        else: #mode가 1일 때
            if code[i] != '1':
                if i%2:
                    answer += code[i]
            else:
                 mode = 0
    if not(answer):
        return "EMPTY"
    print(answer)
    
    return answer