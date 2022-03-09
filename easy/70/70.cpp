#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int X; cin >> X;
    int prices[] = {105, 104, 103, 102, 101, 100};
    vector<bool> dp(X+1, false);
    dp[0] = true;
    for(int i=0; i<=X; i++){
        for(int j=0; j<6; j++){
            if(!dp[i]) continue;
            if(i+prices[j] <= X) dp[i+prices[j]] = true;
        }
    }
    cout << dp[X] << endl;
    return 0;
}