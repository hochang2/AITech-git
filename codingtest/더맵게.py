import heapq
def solution(scoville, K):
    answer = 0
    heap = []
   
    for i in scoville:
        
        heapq.heappush(heap, i)
        
    while(1):
        if heap[0] < K and len(heap)==1:
            return -1
        if heap[0] >= K:
            break
        tem1 = heapq.heappop(heap)
        tem2 = heapq.heappop(heap)
        
        heapq.heappush(heap, tem1 + 2 * tem2)
        answer += 1
    return answer