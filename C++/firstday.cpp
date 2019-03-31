#include <iostream>

using namespace std;
// 1582년 1월 1일이 월요일 일 때,
// 다른 년도의 1월 1일은 몇일인지 계산하는 프로그램

int isLeapYear(int year)
{
    if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)
        return 1;
    else
        return 0;
}

int main()
{
    int times;
    cin >> times;
    for (int i = 0; i < times; i++)
    {
        int year;
        cin >> year;
        int days = 5;
        for (int j = 1582; j < year; j++)
        {
            days += isLeapYear(j) ? 2 : 1;
        }
        cout << days % 7 << endl;
    }
}