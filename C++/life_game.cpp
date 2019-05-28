#include <iostream>

using namespace std;

void fileInput(int *&arr, int num){
    arr = new int[num];
    for(int i=0; i<num; i++){
        cin >> arr[i];
    }
}

void the_time_goes_on(int *&arr, int num,int hour){
	int *arr_r = new int[num];
	for(int i=0; i<num; i++){
		arr_r[i] = arr[i];
	}
    int sum_sides;
        
    for(int i=0; i<hour; i++){
    	for(int j=0; j<num; j++){
            sum_sides = 0;
            if(j == 0){
                sum_sides += arr[j+1];
            }
            else if(j == num-1){
                sum_sides += arr[j-1];
            }
            else{
                sum_sides += arr[j+1];
                sum_sides += arr[j-1];
            }
        	//cout << sum_sides << endl;
            if(arr[j] > 0 && (sum_sides < 3 || sum_sides > 7)) {
            	arr_r[j] -= 1;
            }
            else if(arr[j] < 9 && 3 < sum_sides && sum_sides <= 7) 
            {
	          	arr_r[j] += 1;
            }
            else if(sum_sides == 3) {continue;}
        }
        for(int k=0; k<num; k++){
        	arr[k] = arr_r[k];
        }
    }
}

int main(){
    int *arr;
    int times, num, hour;
    cin >> times;
    for(int i=0; i<times; i++){
        cin >> num >> hour;
        fileInput(arr, num);
        the_time_goes_on(arr, num, hour);
        for(int i=0; i<num; i++){
            cout << arr[i] << " ";
        }
        cout << endl;
    }
}

