#include <algorithm>
#include <climits>
#include <iostream>
#define ll long long

using namespace std;

ll N, M, minTree[4000001], maxTree[4000001], arr[1000001];

ll initTree(int start, int end, int node, bool mode) {
  if (start == end) {
    if (mode) {
      return minTree[node] = arr[start];
    } else {
      return maxTree[node] = arr[start];
    }
  }
  int mid = (start + end) / 2;
  if (mode) {
    return minTree[node] = min(initTree(start, mid, node * 2, mode),
                               initTree(mid + 1, end, node * 2 + 1, mode));
  } else {
    return maxTree[node] = max(initTree(start, mid, node * 2, mode),
                               initTree(mid + 1, end, node * 2 + 1, mode));
  }
}

ll find(int start, int end, int node, int left, int right, bool mode) {
  if (right < start || end < left) {
    if (mode) {
      return LLONG_MAX;
    } else {
      return -1;
    }
  }
  if (left <= start && end <= right) {
    if (mode) {
      return minTree[node];
    } else {
      return maxTree[node];
    }
  }
  int mid = (start + end) / 2;
  if (mode) {
    return min(find(start, mid, node * 2, left, right, mode),
               find(mid + 1, end, node * 2 + 1, left, right, mode));
  } else {
    return max(find(start, mid, node * 2, left, right, mode),
               find(mid + 1, end, node * 2 + 1, left, right, mode));
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }
  initTree(0, N - 1, 1, true);
  initTree(0, N - 1, 1, false);

  ll a, b;
  for (int i = 0; i < M; i++) {
    cin >> a >> b;
    cout << find(1, N, 1, a, b, true) << " " << find(1, N, 1, a, b, false)
         << "\n";
  }
  return 0;
}