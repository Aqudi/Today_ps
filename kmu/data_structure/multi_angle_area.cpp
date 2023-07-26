#include <iostream>

using namespace std;

class P{
public:
    int x, y;
};

void multi_angle_area(P *p, int n){
    int result = 0;
    for(int i=0; i<n; i++){
        result += (p[i].x + p[i+1].x) * (p[i+1].y - p[i].y);
    }
    int sign = result > 0 ? 1 : -1;
    result *= sign;
    cout << result << " " << sign << endl;
}

int main(){
    int times, size, n;
    cin >> times;
    P *p;
    for(int i=0; i<times; i++){
        cin >> size;
        p = new P[size];
        for(int j=0; j<size; j++){
            int x, y;
            cin >> x >> y;
            p[j].x = x;
            p[j].y = y;
        }
        // for(int j=0; j<size; j++){
        //     printf("%d %d \n", p[j].x, p[j].y );
        // }
        multi_angle_area(p, size);
    }
}