#include <iostream>
#include <string>

using namespace std;

int main() {
    string S, T;
    cin >> S >> T;
    int length = S.length();
    for(int i=0; i<length; i++){
        if (S==T){
            cout << "Yes";
            return 0;
        }
        S = S[length-1] + S.substr(0, length-1);
    }
    cout << "No";
    return 0;
}