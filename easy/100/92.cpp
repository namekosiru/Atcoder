#include <iostream>
#include <stack>

using namespace std;

int main() {
    string S;
    cin >> S;
    stack<char> cubes;
    int ans = 0;
    for(int i=0; i<S.length(); i++){
        if(cubes.empty()){
            cubes.push(S[i]);
            continue;
        }
        if(cubes.top() != S[i]){
            cubes.pop();
            ans += 2;
        }else{
            cubes.push(S[i]);
        }        
    }
    cout << ans << endl;

    return 0;
}