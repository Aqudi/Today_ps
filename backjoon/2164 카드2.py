"""
python list 자료구조의 delete, 중간 item pop 연산의 시간복잡도는 O(n)이다.
deque 자료구조의 delete, 중간 item pop 연산의 시간복잡도는 O(1)이다.

이러한 차이는 python list 자료구조는 고정된 크기의 array로 구현되어 있고,
deque의 경우에는 linked list로 구현되어 있기 때문에 발생한다.
"""

from collections import deque

N = int(input())
cards = deque([i for i in range(1, N + 1)], N)
i = 0
while len(cards) > 1:
    item = cards.popleft()
    if i % 2 != 0:
        cards.append(item)
    i += 1
print(cards[0])
