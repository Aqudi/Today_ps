#include <climits>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void mergesort(vector<pair<int, string> >& v, int p, int r);

int main(void) {
  int n;
  vector<pair<int, string> > v;

  cin >> n;

  for (int i = 0; i < n; i++) {
    int d;
    string s;
    cin >> d >> s;
    v.push_back(pair<int, string>(d, s));
  }

  // merge sort
  mergesort(v, 0, v.size() - 1);

  for (int i = 0; i < n; i++) {
    cout << v[i].first << ' ' << v[i].second << endl;
  }

  return 0;
}

void mergesort(vector<pair<int, string> >& v, int p, int r) {
  if (p < r) {
    int q = (p + r) / 2;
    mergesort(v, p, q);
    mergesort(v, q + 1, r);

    vector<pair<int, string> > L, R;
    L.assign(v.begin() + p, v.begin() + q + 1);
    L.push_back(make_pair(INT_MIN, "z"));
    R.assign(v.begin() + q + 1, v.begin() + r + 1);
    R.push_back(make_pair(INT_MIN, "z"));

    int i = 0, j = 0;
    for (int k = p; k <= r; k++) {
      if (L[i].first < R[j].first) {
        v[k] = R[j++];
      } else {
        v[k] = L[i++];
      }
    }
    return;
  }
}