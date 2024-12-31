Y, M, D = map(int, input().split())

daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isYoonYear(year):
    multiple4 = year % 4 == 0
    multiple100 = year % 100 == 0
    multiple400 = year % 400 == 0
    
    if multiple4 and multiple100 and multiple400:
        return True
    
    if multiple4 and multiple100:
        return False

    if multiple4:
        return True
    
    return False

def getDaysInMonth(year, month):
    result = daysInMonth[month-1]
    if month == 2 and isYoonYear(year):
        result += 1
    return result

def solve(year, month, day):
    if day > getDaysInMonth(year, month):
        return -1

    if 3 <= month <= 5:
        return "Spring"
    if 6 <= month <= 8:
        return "Summer"
    if 9 <= month <= 11:
        return "Fall"
    if 12 == month or month <= 2:
        return "Winter"

print(solve(Y, M, D))