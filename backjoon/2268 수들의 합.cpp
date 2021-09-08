#include <iostream>
#define ll long long

using namespace std;

ll N, M, tree[4000001], arr[1000001];

ll sum(int start, int end, int node, int left, int right) {
  if (right < start || end < left)
    return 0;
  if (left <= start && end <= right)
    return tree[node];
  int mid = (start + end) / 2;
  return sum(start, mid, node * 2, left, right) +
         sum(mid + 1, end, node * 2 + 1, left, right);
}

void modify(int start, int end, int node, int index, int diffAmount) {
  if (index < start || index > end)
    return;
  tree[node] += diffAmount;
  if (start == end)
    return;
  int mid = (start + end) / 2;
  modify(start, mid, node * 2, index, diffAmount);
  modify(mid + 1, end, node * 2 + 1, index, diffAmount);
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  cin >> N >> M;
  ll method, a, b;
  for (int i = 0; i < M; i++) {
    cin >> method >> a >> b;
    if (method == 0) {
      if (a > b)
        swap(a, b);
      cout << sum(1, N, 1, a, b) << "\n";
    } else {
      int diffAmount = b - arr[a];
      arr[a] = b;
      modify(1, N, 1, a, diffAmount);
    }
  }
  return 0;
}
