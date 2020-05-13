#include<iostream>

using namespace std;

int count_one(int num){
    int counter = 0;
    while(num >= 1){
        counter += num % 2;
        num  /= 2;
    }
    return counter;
}

long long int Parity_bit(long long int num){
    int ones = count_one(num);
    if(ones % 2 == 1){
        num = num + 2147483648;
    }   
    return num;
}

int main(){
    int time, n;
    cin >> time;
    for (int i=0; i< time; i++){
        cin >> n;
        cout << Parity_bit(n) << endl;
    }
}