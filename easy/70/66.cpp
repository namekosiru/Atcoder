#include <iostream>
#include <map>
using namespace std;

int main() {
    string s;
    cin >> s;
    map<char, int> directMap;
    for(int i=0; i<s.length(); i++){
        if(directMap.count(s[i]))  directMap[s[i]] = 1;
        else directMap[s[i]] = 1;
    }
    if (directMap['N'] != directMap['S']){
        cout << "No" << endl;
        return 0;
    }
    if (directMap['W'] != directMap['E']){
        cout << "No" << endl;
        return 0;
    }

    cout << "Yes" << endl;
    return 0;
}