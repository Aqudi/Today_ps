def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    for i in range(0, len(phone_book)):
        first = phone_book[i]
        for j in range(i+1, len(phone_book)):
            target = phone_book[j]
            if target.startswith(first):
                return False
    return True


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
    print(solution(["12","123","1235","567","88"]))
