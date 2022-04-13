# 다시 푼 문제
# 문제: 프로그래머스 (스택, 큐) 다리를 지나는 트럭
# 문제 설명: truck_weights에 있는 트럭들이 bridge_length 만큼씩만 트럭이 다리에 올라갈 수 있을 때 weight 무게 만큼만
# 버틸 때, 모든 truck들이 다리 지나고 나서의 경과시간
# 풀이법: " 다리를 건너는 트럭" 리스트를 애초에 bridge_length 길이만큼만 설정하고 0으로 초기화 /
# 느낀점: 한번 더 풀어야 할것 같은 느낌


def solution(bridge_length,weight, truck_weights):
    answer = 0 # 경과 시간
    truck_wait = [0 for i in range(bridge_length)] # 다리 건너는 트럭
    while truck_wait: # 다리 건너는 트럭에 값이 있는 동안
        answer += 1
        truck_wait.pop(0)
        if truck_weights: # 대기 리스트가 비어 있지 않은 경우
            if sum(truck_wait) + truck_weights[0] <= weight:
                truck_wait.append(truck_weights.pop(0))
            else:
                truck_wait.append(0)

    return answer


print(solution(2,10,[7,4,5,6]))