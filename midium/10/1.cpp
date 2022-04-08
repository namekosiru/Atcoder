#include <iostream>

using namespace std;

int main() {
    long long N;
    cin >> N;
    long long a[N];
    for(int i=1; i<N+1; i++) cin >> a[i];
    long long count = 0;
    long long nextIndex = 1;
    for(int i=1; i<100100; i++){
        nextIndex = a[nextIndex];
        if (nextIndex==2){
            cout << i << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}