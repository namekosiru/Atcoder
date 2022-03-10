#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    long long A[N];
    long long total[N+1];
    long long left=0, right=0; 
    long long ans = 1e12;

    for(int i=0; i<N; i++) cin >> A[i];
    total[0] = 0ll;
    for(int i=1; i<N+1; i++){
        total[i] = total[i-1]+A[i-1];
    }
    for(int i=1; i<N; i++){
        ans = min(ans, abs(total[i] - (total[N] - total[i])));
    }

    cout << ans << endl;
    return 0;
}