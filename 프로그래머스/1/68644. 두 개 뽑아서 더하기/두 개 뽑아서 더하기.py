def solution(numbers):
    answer = []
    number_length = len(numbers)
    for i in range(number_length-1):
        for j in range(i+1, number_length):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer = sorted(answer)
    return answer