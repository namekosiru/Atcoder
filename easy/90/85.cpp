#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int D, N;
    cin >> D >> N;
    if (N==100) N++;
    long long ans = pow(100, D)*N;
    cout << ans << endl;
    return 0;
}