def solution(no, works):
    for i in range(no):
        works = sorted(works, reverse=True)
        works[0] -= 1
    
    result = 0
    for w in works:
        if w > 0:
	        result += w ** 2
    
    if result < 0:
        result = 0
    return result