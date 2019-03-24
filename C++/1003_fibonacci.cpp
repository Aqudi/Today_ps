#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{

    int memo[41][2] = {
        0,
    };
    memo[0][0] = 1;
    memo[0][1] = 0;
    memo[1][0] = 0;
    memo[1][1] = 1;
    memo[2][0] = 1;
    memo[2][1] = 1;

    int times;
    cin >> times;
    for (int i = 1; i <= times; i++)
    {
        int n;
        cin >> n;
        for (int j = 2; j <= n; j++)
        {
            if (memo[n][0] != 0 || memo[n][1] != 0)
            {
                break;
            }
            else
            {
                memo[j][0] = memo[j - 1][0] + memo[j - 2][0];
                memo[j][1] = memo[j - 1][1] + memo[j - 2][1];
            }

            // printf("memo[%d][0] =  %d memo[%d][0] = %d ==> memo[%d][0] = %d\n", j - 1, memo[j - 1][0], j - 2, memo[j - 2][0], j, memo[j][0]);
            // printf("memo[%d][1] =  %d memo[%d][1] = %d ==> memo[%d][1] = %d\n\n", j - 1, memo[j - 1][1], j - 2, memo[j - 2][1], j, memo[j][0]);
        }
        printf("%d %d\n", memo[n][0], memo[n][1]);
    }
}