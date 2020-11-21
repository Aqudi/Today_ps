def solution(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    
    score = 0
    i, j = 0, 0
    for k in range(len(A)):
        if A[i] > B[j]:
            i += 1
        elif A[i] == B[j]:
            i += 1
        elif A[i] < B[j]:
            score += 1
            i += 1
            j += 1
    return score