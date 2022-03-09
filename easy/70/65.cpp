#include <iostream>

using namespace std;

int main() {
    string s;
    cin >> s;
    int ans = 0;
    int count = 0;
    bool flag = false;
    int ai=1e+9, zi;
    for(int i=0; i<s.length(); i++){
        if (s[i] == 'A'){
            if (ai > i) ai = i;
        }
        if (s[i] == 'Z'){
            zi = i;
        }
    }
    cout << zi - ai + 1 << endl;
    return 0;
}