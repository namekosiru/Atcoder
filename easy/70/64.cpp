#include <iostream>

using namespace std;

int main() {
    string O, E;
    cin >> O >> E;
    string ans;
    int maxSize = max(O.length(), E.length());
    for(int i=0; i<maxSize; i++){
        if (i<O.length()){
            ans += O[i];
        }
        if (i<E.length()){
            ans += E[i];
        }
    }
    cout << ans << endl;
    return 0;
}