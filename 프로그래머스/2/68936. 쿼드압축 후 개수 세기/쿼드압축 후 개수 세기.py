def quad_zip(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if sum(sum(arr, [])) == 0:
        return [0]
    if sum(sum(arr, [])) == n ** 2:
        # print(arr)
        return [1]
    else:
        TL = [elem[:n//2] for elem in arr[:n//2]]
        TR = [elem[n//2:] for elem in arr[:n//2]]
        BL = [elem[:n//2] for elem in arr[n//2:]]
        BR = [elem[n//2:] for elem in arr[n//2:]]

        return quad_zip(TL) + quad_zip(TR) + quad_zip(BL) + quad_zip(BR)


def solution(arr):
    answer = []
    n = len(arr)
    quad = quad_zip(arr)
    # print(quad)
    answer = [len(quad) - sum(quad), sum(quad)]
    return answer 
