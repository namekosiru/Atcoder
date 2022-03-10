#include <iostream>
#include <cmath>

using namespace std;
using ll = long long;


int main() {
    int X; cin >> X;
    int ans = 0;
    for(int i=1; i<=1000; i++){
        for(int j=2; j<=10; j++){
            int value = pow(i, j);
            if(value <= X){
                ans = max(ans, value);
            }
        }
    }
    cout << ans << endl;
    return 0;
}