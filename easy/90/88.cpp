#include <iostream>
#include <map>

using namespace std;

int main() {
    int N, M;
    cin >> N;
    map<string, int> sMap;
    map<string, int> tMap;
    for(int i=0; i<N; i++){
        string s;
        cin >> s;
        if(sMap.count(s) == 0){
            sMap[s] = 1;
        }else{
            sMap[s] += 1;
        }
    }
    cin >> M;
    for(int i=0; i<M; i++){
        string t;
        cin >> t;
        if(tMap.count(t)==0){
            tMap[t] = 1;
        }else {
            tMap[t] += 1;
        }
    }
    int ans = 0;
    for(auto iter=sMap.begin(); iter!=sMap.end(); iter++){
        if(tMap.count(iter->first) == 0){
            ans = max(ans, sMap[iter->first]);
        }else{
            ans = max(ans, sMap[iter->first]-tMap[iter->first]);
        }
    }
    if (ans<0){
        cout << ans << endl;
        return 0;
    }
    cout << ans << endl;
    return 0;
}