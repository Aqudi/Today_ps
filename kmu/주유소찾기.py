def solution(gas, cost):
    costs = [g - c for g, c in zip(gas, cost)]
    
    if sum(costs) < 0:
        return -1
    
    sparse = [0]
    sparseIdx = [0]
    
    idx = 0
    code = costs[0] >= 0
    for i, cost in enumerate(costs):
        temp = cost >= 0
        if code != temp:
            idx += 1
            sparseIdx.append(i)
            code = not code
            sparse.append(cost)
        else:
            sparse[idx] += cost
        # print(sparse)
    if sparse[-1] * sparse[0] >= 0:
        sparse[0] += sparse.pop()
        sparseIdx[0] = sparseIdx.pop()
    if sparse[0] < 0:
        temp = sparse.pop(0)
        sparse.append(temp)
        temp = sparseIdx.pop(0)
        sparseIdx.append(temp)
        
    # print(sparse, sparseIdx)

    total = 0
    remain = 0
    
    answer = 0
    for i, s in enumerate(sparse):
        total += s
        if total < 0:
            answer = i + 1
            remain = total
            total = 0
    # print(total, answer, remain)
    if total - remain < 0:
        return -1
    return sparseIdx[answer]
    