#include <stdio.h>
#include <iostream>
using namespace std;


int arr[500][500];

int max(int a, int b) {
	return (a >= b) ? a : b;
}

int find_max(int n, int arr_m[][500]) {
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			int f = arr_m[i][j] + arr_m[i - 1][j];
			int s;
			if (arr_m[i - 1][j - 1]) {
				s = arr_m[i][j] + arr_m[i - 1][j - 1];
			}
			else {
				s = 0;
			}
			arr[i][j] = max(f, s);
		}
	}
	/*
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i + 1; j++)
		{
			cout << arr_m[i][j] << " ";
		}
		cout << endl;
	}
	*/
	int max_num = arr_m[n-1][0];
	for (int i = 1; i < n; i++) {
		int target = arr_m[n-1][i];
		max_num = (max_num > target) ? max_num : target;
	}

	return max_num;
}

int main()
{
	int n;
	scanf("%d", &n);
	int max_col = 1;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i+1; j++)
		{
			int value;
			scanf("%d", &value);
			arr[i][j] = value;
		}
	}

	int result = find_max(n, arr);
	cout << result << "\n";
		
	return 0;
}