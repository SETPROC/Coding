def solution(bandage, health, attacks):
    
    # t는 가장 긴 타임을 구한다.
    t = max(attacks,key=lambda x: x[0])[0]
    # c는 회복 타임 계산을 위한 변수
    c = 0
    
    # attacks를 접근하기 위한 인덱스 변수 idx
    idx = 0
    
    # 반복문을 위한 변수 i
    # i = 1
    
    # 최대 체력을 담을 변수 h_max
    h_max = health
    
    for i in range(0,t+1):
        print(i,health,c,idx)
        if health <= 0:
            return -1
        else:
            #어택 당할 경우
            if attacks[idx][0] == i:
                if health - attacks[idx][1] > 0:
                    health  -= attacks[idx][1]
                    c = 0
                    idx += 1
                    print(i,health,c,idx)
                else:
                    return -1
            else:
                # 어택 안 당할 경우
                if health + bandage[1] >= h_max:
                    health = h_max
                    c += 1
                    print(i,health,c,idx)
                else:
                    health += bandage[1]
                    c += 1
                    print(i,health,c,idx)
                
                if c == bandage[0]:
                    if health + bandage[2] >= h_max:
                        health = h_max
                        c = 0
                        print(i,health,c,idx)
                    else:
                        health += bandage[2]
                        c = 0
                        print(i,health,c,idx)
    return health
                
                    
                    
            
        
   