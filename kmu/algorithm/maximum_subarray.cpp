#include <climits>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef struct tuple3 {
  int i;
  int j;
  int k;
} tuple3_t;

tuple3_t find_maximum_crossing_subarray(vector<int> v, int low, int mid,
                                        int high) {
  int left = INT_MIN, right = INT_MIN;
  int max_left, max_right;

  int sum = 0;
  for (int i = mid; i >= low; i--) {
    sum += v[i];
    if (sum > left) {
      left = sum;
      max_left = i;
    }
  }

  sum = 0;
  for (int i = mid + 1; i <= high; i++) {
    sum += v[i];
    if (sum > right) {
      right = sum;
      max_right = i;
    }
  }

  tuple3_t result;
  result.i = max_left;
  result.j = max_right;
  result.k = right + left;
  return result;
}

tuple3_t find_maximum_subarray(vector<int> v, int low, int high) {
  tuple3_t result;
  if (high == low) {
    result.i = low;
    result.j = high;
    result.k = v[low];
    return result;
  } else {
    int mid = (low + high) / 2;
    tuple3_t left = find_maximum_subarray(v, low, mid);
    tuple3_t right = find_maximum_subarray(v, mid + 1, high);
    tuple3_t cross = find_maximum_crossing_subarray(v, low, mid, high);

    if (left.k >= right.k && left.k >= cross.k)
      return left;
    else if (right.k >= left.k && right.k >= cross.k)
      return right;
    else
      return cross;
  }
}

int solution(vector<int> param0) {
  tuple3_t result = find_maximum_subarray(param0, 0, param0.size() - 1);
  int answer = result.k;
  return answer;
}

int main(void) {
  int n;
  vector<int> v;

  cin >> n;

  for (int i = 0; i < n; i++) {
    int d;
    cin >> d;
    v.push_back(d);
  }

  int answer = solution(v);
  cout << answer << endl;

  return 0;
}