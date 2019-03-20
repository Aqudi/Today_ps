#include<iostream>
using namespace std;

void outputPyramid(int n, int k);

int main(void){
	
	int t;
	int n, k;
	
	cin >> t;
	
	for(int i=0; i<t; i++){
		cin >> n >> k;
		outputPyramid( n, k );
	}
	return 0;
}

void outputPyramid(int n, int k){
	int adder = n-1;
	int added = k;
	cout << k;
	for (int i=0; i<k-1; i++){
        added += adder;
        cout << "*" << added;
        adder--;
	}
    cout << endl;
}
