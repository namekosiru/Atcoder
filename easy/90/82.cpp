#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int main() {
    long long Q, H, S, D, N;
    cin >> Q >> H >> S >> D >> N;

    H = min(H, 2*Q);
    S = min(S, 2*H);
    if(2*S <= D){
        cout << S * N << endl;
        return 0;
    }else{
        cout << (N/2)*D + (N%2)*S << endl; 
        return 0;
    }
    return 0;
}