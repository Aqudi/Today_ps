#include <iostream>
using namespace std;
int closestNumber(int n, int m);
int abs_num(int num);

int main(void)
{
int t;
int n, m;
    cin >> t;
    for(int i=0; i<t; i++)
{
        cin >> n >> m;
        cout << closestNumber( n, m ) << endl;
    }
    return 0;
}
int closestNumber(int n, int m)
{   
    int sign = n / abs_num(n);
    n = abs_num(n);
    m = abs_num(m);
    return (n % m >= m / 2) ? sign * (n + m - n % m) : sign * (n - n % m); 

}
int abs_num(int num){
    return (num > 0) ? num : -num;
}