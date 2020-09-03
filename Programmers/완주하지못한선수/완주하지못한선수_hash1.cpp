#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

string solution(vector<string> participant, vector<string> completion);

int main() {
  vector<string> p, c;
  int n;
  string s;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> s;
    p.push_back(s);
  }
  for (int i = 1; i < n; i++) {
    cin >> s;
    c.push_back(s);
  }

  string answer = solution(p, c);
  cout << answer << endl;
}

string solution(vector<string> participant, vector<string> completion) {
  string answer = "";
  unordered_set<string> m;

  for (size_t i = 0; i < completion.size(); i++) {
    m.insert(completion[i]);
  }

  for (size_t i = 0; i < participant.size(); i++) {
    auto it = m.find(participant[i]);
    if (m.end() == it) {
      answer = participant[i];
      break;
    }
    m.erase(it);
  }
  return answer;
}
