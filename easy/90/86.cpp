#include <iostream>

using namespace std;

int main() {
    string S;
    cin >> S;
    int K;
    cin >> K;
    int index = 0;
    while(K>0){
        if(S[index] == '1'){
            K--;
            index++;
        }
        else{
            cout << S[index] << endl;
            return 0;
        }
    }
    cout << 1 << endl;
    return 0;
}