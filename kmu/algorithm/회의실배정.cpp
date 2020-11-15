#include <algorithm>
#include <vector>
using namespace std;

bool cmp(const vector<int> &a, const vector<int> &b) {
    if(a[1] == b[1]) {
        return a[0] < b[0];
    }
    return a[1] =< b[1];
}

int solution(vector<vector<int> > arr) {
    sort(arr.begin(), arr.end(), cmp);
    
    int answer = 1;
    
    int k = 0;
    for(int m=1; m < arr.size(); m++) { 
        if(arr[m][0] >= arr[k][1]) {
            answer += 1;
            k = m;
        }
    }
    return answer;
}