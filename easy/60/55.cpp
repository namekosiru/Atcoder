#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

float calcDistance(int pos1[], int pos2[], int D){
    int distance = 0;
    for (int i=0; i<D; i++){
        distance += (pos1[i] - pos2[i]) * (pos1[i] - pos2[i]);
    }
    return sqrt(distance);
}

int main() {
    int N, D;
    cin >> N >> D;
    int pos[N][D];
    for (int i=0; i<N; i++){
        for(int j=0; j<D; j++){
            cin >> pos[i][j];
        }
    }
    float distance;
    int ans = 0;
    for (int i=0; i<N; i++){
        for(int j=i+1; j<N; j++){
            distance = calcDistance(pos[i], pos[j], D);
            if (ceil(distance) == distance){
                ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}