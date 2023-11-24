#include<iostream>

using namespace std;

class P{
public:
    int x, y;
};

void triangle_area(P *ps){
    int area;
    ps[1].x -= ps[0].x;
    ps[1].y -= ps[0].y;
    ps[2].x -= ps[0].x;
    ps[2].y -= ps[0].y;
    area = (ps[1].x * ps[2].y - ps[1].y * ps[2].x);

    int sign =  (area > 0) ? 1 : (area == 0) ? 0 : -1;
    area = area * sign;
    cout << area << " " << sign << endl;
}

int main(){
    int times;
    cin >> times;
    P ps[3];
    for(int i=0; i<times; i++){
        for(int j=0; j<3; j++){
            int x, y;
            cin >> x >> y;
            ps[j].x = x;
            ps[j].y = y;
        }
        triangle_area(ps);
    }
}