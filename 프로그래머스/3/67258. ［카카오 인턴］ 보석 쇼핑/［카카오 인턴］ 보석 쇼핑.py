def solution(gems):
    gem_names = set(gems)
    gem_number = len(gem_names)
    full_length = len(gems)
    start_index = 0
    end_index = 0
    answer = [start_index, end_index]
    min_length = 1000001
    partition_dict = {}
    while end_index < full_length + 1:
        check = len(partition_dict) == gem_number
        if not check and end_index != full_length:
            end_gem = gems[end_index]
            if end_gem not in partition_dict:
                partition_dict[end_gem] = 1
            else:
                partition_dict[end_gem] += 1
            end_index +=1
            continue
        if not check and end_index == full_length:
            break
        if min_length > end_index - start_index + 1:
            min_length = end_index - start_index + 1
            answer = [start_index + 1, end_index]
        start_gem = gems[start_index]
        partition_dict[start_gem] -= 1   
        if partition_dict[start_gem] == 0:
            partition_dict.pop(start_gem)
        start_index += 1     
    return answer