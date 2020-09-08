#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> sub;
    for(auto& it: commands){
        int i = it[0];
        int j = it[1];
        int k = it[2];
        sub.assign(array.begin() + i-1, array.begin() + j);
        sort(sub.begin(), sub.end());
        answer.push_back(sub[k-1]);
        sub.clear();
    }
    return answer;
}