import heapq

# 우선순위 큐 => heapq 사용
# 가장 맵기 지수가 낮은 두 음식을 뽑아(pop) 문제 조건에 맞게 연산한 뒤, 다시 push

def solution(scoville, K):
    
    # answer: 몇 번 음식을 섞었는 지 세기 위한 변수
    answer = 0
    heap = []
   
    for i in scoville:
        
        # 우선 순위큐 (= heap), 오름차순
        heapq.heappush(heap, i)
        
    while(1):
        
        # 음식이 하나 남았는 데 맵기가 주어진 K 보다 작은 경우 -> 모든 음식을 K 이상으로 못 만드는 경우
        # return -1
        if heap[0] < K and len(heap)==1:
            return -1
        
        # 제일 맵기가 낮은 음식이 주어진 K 이상이면 -> 반복문 종료
        if heap[0] >= K:
            break
        
        # 맵기가 작은 두 음식 뽑아 오기 -> pop를 사용하면 heap에서 값을 삭제하고, 반환한다
        tem1 = heapq.heappop(heap)
        tem2 = heapq.heappop(heap)
        
        # 문제에서 주어진 연산 조건에 맞게 push
        heapq.heappush(heap, tem1 + 2 * tem2)
        answer += 1
    return answer