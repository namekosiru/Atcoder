#include <iostream>

#define rep(i, n) for(int i=0; i<n; i++)

using namespace std;

int main() {
    int N;
    cin >> N;
    int T[N];
    rep(i, N) cin >> T[i];
    int M;
    cin >> M;
    int P, X;
    rep(i, M){
        int timeSum = 0;
        cin >> P >> X;
        rep(i, N){
            if (i+1 == P){
                timeSum += X;
            }else{
                timeSum += T[i];
            }
        }
        cout << timeSum << endl;
    }
    return 0;
}