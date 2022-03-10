#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<int>> a(2, vector<int>(N, 0));
    for(int i=0; i<2; i++){
        for(int j=0; j<N; j++){
            cin >> a[i][j];
        }
    }
    long long ans = 0;
    for(int i=0; i<N; i++){
        long long sum = 0;
        for(int k=0; k<=i; k++){
            sum += a[0][k];
        }
        for(int j=i; j<N; j++){
            sum += a[1][j];
        }
        ans = max(ans, sum);
    }
    cout << ans << endl;
    return 0;
}