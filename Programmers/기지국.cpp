#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int solution(int n, vector<int> stations, int w) {
  int count = 0;

  int width = 2 * w + 1;
  int last = 0;
  for (int station : stations) {
    int left = station - w - 1;
    int right = station + w;

    float remain = left - last;

    if (remain >= 0) {
      count += ceil(remain / width);
    }
    last = right;
  }
  // 마지막 staion이 커버하는 범위가 n보다 작을 때
  if (last < n) {
    float remain = n - last;
    if (remain > 0) {
      count += ceil(remain / width);
    }
  }
  return count;
}