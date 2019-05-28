#include <iostream>
#include <algorithm>

using namespace std;

unsigned int data[7410];

unsigned int hamingNumber(int k)
{
    int idx = 0;
    unsigned int max = 1000000000;
    unsigned int two, three, five;
    for(two = 1; ; two*=2){
        for( three = two; ; three*=3){
            for(five=three; ; five*=5){
                data[idx++] = five;
                if(five>max/5) break;
            }
            if(three>max/3) break;
        }
        if(two>max/2) break;
    }
    sort(data, data+idx);
	return data[k - 1];
}

int main()
{
	int times, k;
	cin >> times;
	for (int i = 0; i < times; i++)
	{
		cin >> k;
		cout << hamingNumber(k) << endl;
	}
}