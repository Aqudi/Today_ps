#include <iostream>
using namespace std;
void outputZigZag(int n, int k);
int main(void)
{
int t;
int n, k;
    cin >> t;
    for(int i=0; i<t; i++)
{
        cin >> n >> k;
        outputZigZag( n, k );
    }
    return 0;
}
void outputZigZag(int n, int k)
{	
		int start_num = k * (k-1) * 0.5 + 1;
		int end_num = start_num + k - 1;
		if (k % 2 == 0){
			cout << end_num;
			for (int i=1; i < k; i++){
				cout << "*" << end_num-i;
			}	
		}
		else{
			cout << start_num;
			for (int i=1; i < k; i++){
				cout << "*" << start_num+i;
			}	
		}
		cout << endl;
}
