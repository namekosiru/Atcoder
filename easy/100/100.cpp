#include <iostream>

using namespace std;

int main() {
    long long N;
    cin >> N;
    long long a[N];
    for(int i=0; i<N; i++){
        cin >> a[i];
    }
    int ans = 0;
    for(int i=0; i<N; i++){
        if((i+1)==a[a[i]-1]){
            ans++;
        }
    }
    cout << ans/2 << endl;
    return 0;
}