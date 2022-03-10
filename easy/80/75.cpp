#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

int main() {
    int N, K;
    cin >> N >> K;
    vector<ll> h(N);
    long long ans = 10e9;
    for(int i=0; i<N; i++) cin >> h[i];
    sort(h.begin(), h.end());
    for(int i=0; i<N-K+1; i++){
        ans = min(ans, h[i+K-1]-h[i]);
    }
    cout << ans << endl;
    return 0;
}