#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
  int n;
  cin >> n;

  map<string, int> m;
  string temp;
  for (int i = 0; i < n; i++) {
    cin >> temp;
    m[temp]++;
  }

  int max = 0;
  string book = "";

  for (auto it = m.begin(); it != m.end(); it++) {
    if (it->second > max) {
      max = it->second;
      book = it->first;
    }
  }
  cout << book << endl;
}