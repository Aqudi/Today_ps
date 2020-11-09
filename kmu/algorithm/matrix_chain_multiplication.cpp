#include <vector>
#include <climits>
#include <iostream>

using namespace std;


int main(void) {
    int n;
    vector<int> v;

    cin >>  n;
    for (int i=0; i<n+1; i++){
        int d;
        cin >> d;
        v.push_back(d);
    }
    
    n = v.size();
    int m[1001][1001];
        
    for(int i=1; i<n; i++){
        m[i][i] = 0;
    }
    
    for(int l=2; l<n; l++) {
        for(int i=1; i< n - l + 1; i++) {
            int j = i + l - 1;
            m[i][j] = INT_MAX;
            for (int k=i; k < j; k++) {
                int q = m[i][k] + m[k+1][j] + v[i-1] * v[k] * v[j];
                if(q < m[i][j]) {
                    m[i][j] = q;
                }
            }
        }
    }
    // for(int i=1; i<n; i++){
    //     for(int j=1; j<n; j++){
    //         cout << m[i][j] << "\t";
    //     }
    //     cout << endl;
    // }
    
    cout << m[1][n-1];
    return 0;
}