#include <iostream>
#include <math.h>

using namespace std;

int main() {
    long long X, Y;
    cin >> X >> Y;
    long long w = Y / X;

    int ans = 0;
    while (X*2 <= Y){
        X *= 2;
        ans ++;
    }
    cout << ans+1 << endl;
    return 0;
}