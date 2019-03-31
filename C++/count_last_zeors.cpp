#include <iostream>
#include <cmath>

using namespace std;

int countLastZeros();

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cout << countLastZeros() << endl;
	}
}

int countLastZeros()
{
	int times;
	cin >> times;
	unsigned int nums[101];
	for (int i = 0; i < times; i++)
	{
		cin >> nums[i];
	}

	int two = 0;
	int five = 0;

	for (int i = 0; i < times; i++)
	{
		int num = nums[i];
		while (num % 2 == 0)
		{	
			num /= 2;
			two++;
		}
		num = nums[i];
		while (num % 5 == 0)
		{
			num /= 5;
			five++;
		}
	}
	return (two > five) ? five : two;
}