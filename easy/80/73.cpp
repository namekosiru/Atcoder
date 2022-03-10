#include <iostream>
#include <cmath>

using namespace std;
using ll = long long;

int main() {
    ll N; cin >> N;
    N++;
    ll res = 0;
    while (N) {
        if (N<10) res += N-1;
        else res += 9;
        N /= 10;
    }
    cout << res << endl;
    return 0;
}