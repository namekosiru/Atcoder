#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<long long>> v_list(N, vector<long long>(2));
    for(int i=0; i<N; i++){
        long long A, B;
        cin >> A >> B;
        v_list[i][0] = A; v_list[i][1] = B;
    }
    sort(v_list.begin(), v_list.end());

    long long ans = 0;
    for(int i=0; i<N; i++){
        if(v_list[i][1] <= M){
            ans += v_list[i][0] * v_list[i][1];
            M -= v_list[i][1];
        }else{
            ans += v_list[i][0] * M;
            break;
        }
    }
    cout << ans << endl;

    return 0;
}