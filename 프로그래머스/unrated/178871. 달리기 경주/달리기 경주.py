def solution(players, callings):
    answer = players
    rank_dict = {player:rank for rank, player in enumerate(players)}

    for player in callings:
        rank = rank_dict[player]
        rank_dict[player] = rank-1
        rank_dict[answer[rank-1]] = rank
        answer[rank], answer[rank-1] = answer[rank-1], answer[rank]
    return answer