#include <algorithm>
#include <iostream>
#include <list>
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

int HASH_SIZE = 10000;
string solution(vector<string> participant, vector<string> completion) {
  string answer = "";
  hash<string> h;
  list<string> e;
  vector<list<string>> t(HASH_SIZE, e);

  for (auto it = completion.begin(); it != completion.end(); it++) {
    int hashValue = h(*it) % HASH_SIZE;
    t[hashValue].push_back(*it);
  }

  for (auto it = participant.begin(); it != participant.end(); it++) {
    int hashValue = h(*it) % HASH_SIZE;
    bool notFound = true;
    for (auto bit = t[hashValue].begin(); bit != t[hashValue].end(); bit++) {
      if (*bit == *it) {
        notFound = false;
        t[hashValue].erase(bit);
        break;
      }
    }
    if (notFound) {
      answer = *it;
      break;
    }
  }
  return answer;
}