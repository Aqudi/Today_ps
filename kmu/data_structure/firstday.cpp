#include <iostream>

using namespace std;
// 1582�� 1�� 1���� ������ �� ��,
// �ٸ� �⵵�� 1�� 1���� �������� ����ϴ� ���α׷�

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