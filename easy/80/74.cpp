#include <iostream>

using namespace std;


int main() {
    long long A, B, C, X, Y;
    cin >> A >> B >> C >> X >> Y;
    long long ans = 10e8;
    long long minNum = min(X, Y);
    long long maxNum = max(X, Y);
    // それぞれ買う
    ans = min(ans, X*A+Y*B);
    // 最小単位だけ買う
    if(minNum == X){
        long long value = 2*minNum*C+(Y-minNum)*B; 
        ans = min(ans, value);
    }else{
        long long value = 2*minNum*C+(X-minNum)*A; 
        ans = min(ans, value);
    }
    ans = min(ans, 2 * maxNum * C);
    cout << ans << endl;
    return 0;
}