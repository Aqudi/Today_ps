#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays);

template <typename T>
void pirntVector(vector<T> v) {
  for (auto it = v.begin(); it != v.end(); it++) {
    cout << *it << endl;
  }
}

int main() {
  vector<string> g;
  vector<int> p;
  int n;
  cin >> n;

  string s;
  for (int i = 0; i < n; i++) {
    cin >> s;
    g.push_back(s);
  }
  for (int i = 0; i < n; i++) {
    cin >> s;

    p.push_back(stoi(s));
  }

  vector<int> answer = solution(g, p);
  pirntVector<int>(answer);
  return 0;
}

template <typename T1, typename T2>
bool cmp(pair<T1, T2>& a, pair<T1, T2>& b) {
  if (a.second != b.second) return a.second > b.second;
  return a.first < b.first;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
  vector<int> answer;

  unordered_map<string, int> score_map;
  unordered_map<string, vector<pair<int, int>>> musics;

  for (int i = 0; i < genres.size(); i++) {
    if (score_map.count(genres[i]) == 0) {
      score_map[genres[i]] = 0;
      musics[genres[i]] = vector<pair<int, int>>();
    }
    score_map[genres[i]] += plays[i];
    musics[genres[i]].push_back(make_pair(i, plays[i]));
  }

  // 많이 팔린 장르순으로 정렬
  vector<pair<string, int>> scores;
  for (auto& it : score_map) {
    scores.push_back(it);
  }
  sort(scores.begin(), scores.end(), cmp<string, int>);

  // 많이 팔린 곡별로 정로
  for (auto& it : scores) {
    sort(musics[it.first].begin(), musics[it.first].end(), cmp<int, int>);
  }

  for (auto& it : scores) {
    answer.push_back(musics[it.first][0].first);
    if (musics[it.first].size() >= 2)
      answer.push_back(musics[it.first][1].first);
  }

  return answer;
}

/*
5
classic
pop
classic
classic
pop
500
600
150
800
2500
*/