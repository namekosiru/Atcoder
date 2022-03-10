#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
using ll = long long;

int main() {
    ll N;
    cin >> N;
    vector<ll> a(3*N);
    for(ll i=0; i<3*N; i++) cin >> a[i];
    sort(a.begin(), a.end(), greater<ll>());
    ll ans = 0;
    for(ll i=1, j=0; j<N; i+=2, j++) ans += a[i];
    cout << ans << endl;
    return 0;
}