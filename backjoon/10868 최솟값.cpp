#include <algorithm>
#include <climits>
#include <iostream>
#define ll long long

using namespace std;

ll N, M, tree[4000001], arr[1000001];

ll initTree(int start, int end, int node) {
  if (start == end) {
    return tree[node] = arr[start];
  }
  int mid = (start + end) / 2;
  return tree[node] = min(initTree(start, mid, node * 2),
                          initTree(mid + 1, end, node * 2 + 1));
}

ll findMin(int start, int end, int node, int left, int right) {
  if (right < start || end < left) {
    return LLONG_MAX;
  }
  if (left <= start && end <= right) {
    return tree[node];
  }
  int mid = (start + end) / 2;
  return min(findMin(start, mid, node * 2, left, right),
             findMin(mid + 1, end, node * 2 + 1, left, right));
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }
  initTree(0, N - 1, 1);

  ll a, b;
  for (int i = 0; i < M; i++) {
    cin >> a >> b;
    cout << findMin(1, N, 1, a, b) << "\n";
  }
  return 0;
}