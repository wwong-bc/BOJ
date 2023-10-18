def solution(scores):
    wanho = scores[0]
    new_score = sorted(scores, key = lambda elem: [elem[0], -elem[1]],reverse=True)
    incentive_list = []
    max_score = -1
    current_score = 0
    for score in new_score:
        if not incentive_list:
            incentive_list.append(score)
            current_score = score[0]
            max_score = score[1]
            continue
        if score[0] < current_score and score[1] < max_score:
            continue
        else:
            incentive_list.append(score)
            max_score = score[1]
            
    if wanho not in incentive_list:
        return -1
    sum_list = [elem[0]+ elem[1] for elem in incentive_list]
    sum_list = sorted(sum_list, reverse= True)
    answer = sum_list.index(wanho[0] + wanho[1]) + 1
    return answer