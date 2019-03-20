#include <iostream>
using namespace std;
int angleClock(int h, int m);
int main(void)
{
int t;
int h, m;
    cin >> t;
    for(int i=0; i<t; i++)
{
        cin >> h >> m;
        cout << angleClock( h, m ) << endl;
    }
    return 0;
}
int angleClock(int h, int m)
{
    double doo = (h * 30 - 5.5 * m) ;
	if (doo < 0) {
		doo += 360;
	}
	doo = (doo < 360-doo) ? doo : 360 - doo;
	return doo;
}
