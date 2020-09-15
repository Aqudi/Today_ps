#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main(void) {
    int n;
    vector<pair<int, string> > v;
    
    cin >> n;
    
    for (int i=0; i<n; i++){
        int d;
        string s;
        cin >> d >> s;  
        v.push_back(pair<int,string>(d,s));
    }
    
    // insertion sort
    for(int i=1; i<v.size(); i++){
        for(int j=i; j>0; j--){
            if(v[j].first >= v[j-1].first){
                break;
            }
            swap(v[j], v[j-1]);            
        }
    }
    
    // output 
    for (int i=0; i<n; i++){
        cout << v[i].first << ' ' << v[i].second << endl;          
    }

    return 0;
}