n = int(input())

# Write your code here!
cursor = n
count = 0
result = 1

while count != n:
    count = cursor - (cursor // 3 + cursor // 5 - cursor // 15)
    cursor += n - count

print(cursor)
