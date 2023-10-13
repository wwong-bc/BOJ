import heapq

def solution(n, works):
    full_works = sum(works)
    if n > full_works:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    answer = square_sum(works)
    return answer

def square_sum(work_list):
    work_sum = 0
    for work in work_list:
        work_sum += work ** 2
    return work_sum