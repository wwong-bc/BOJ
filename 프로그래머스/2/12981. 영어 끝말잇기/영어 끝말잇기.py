def solution(n, words):
    word_dict = {}
    answer = [0, 0]
    previous_end = ""   
    for i, word in enumerate(words):
        if i == 0:
            word_dict[word] = 1
            previous_end = word[-1]
            continue
        if word in word_dict:
            return  [i%n + 1, i//n + 1]
        if word[0] != previous_end:
            return  [i%n + 1, i//n + 1]
        previous_end = word[-1]
        word_dict[word] = 1
    return answer


