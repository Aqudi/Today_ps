def solution(answers):
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    lengths = [len(x) for x in patterns]
    
    scores = [0, 0, 0]
    for i, answer in enumerate(answers):
        idxs = [i % length for length in lengths]
        for j in range(3):
            scores[j] += patterns[j][idxs[j]] == answer
    
    answer = []
    max_score = max(scores)
    for i in range(len(scores)):
        if max_score == scores[i]:
            answer.append(i+1)
    return answer