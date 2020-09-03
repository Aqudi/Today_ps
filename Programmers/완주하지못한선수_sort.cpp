#include <algorithm>
#include <iostream>
#include <string>
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
  sort(participant.begin(), participant.end());
  sort(completion.begin(), completion.end());
  for (int i = 0; i < completion.size(); i++) {
    if (participant[i] != completion[i]) return participant[i];
  }
  return participant[participant.size() - 1];
}