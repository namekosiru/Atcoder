#include <iostream>

#define yes "AC"
#define no "WA"

using namespace std;

string solve(string S) {
    int n = S.length();
    if (S[0] != 'A') return no;
    if (S[1] < 'a'|| 'z' < S[1]) return no;
       if (S[n-1] < 'a' or 'z' < S[n-1]) return no;
 
    int C = 0, x = 0;
    for (int i=2; i<n-1; i++) {
        if ('a' <= S[i] and S[i] <= 'z') x++;
        else if (S[i] == 'C') C++;
        else return no;
    }
    if (C == 1) return yes;
    return no;

}

int main() {
    string character;
    cin >> character;
    cout << solve(character);
    return 0;
}