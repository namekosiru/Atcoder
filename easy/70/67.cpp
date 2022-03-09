#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;i++)
#define rrep(i,a,b) for(int i=a;i>=b;i--)
#define fore(i,a) for(auto &i:a)
#define all(x) (x).begin(),(x).end()
//#pragma GCC optimize ("-O3")
using namespace std; void _main(); int main() { cin.tie(0); ios::sync_with_stdio(false); _main(); }
typedef long long ll; const int inf = INT_MAX / 2; const ll infl = 1LL << 60;
template<class T>bool chmax(T& a, const T& b) { if (a < b) { a = b; return 1; } return 0; }
template<class T>bool chmin(T& a, const T& b) { if (b < a) { a = b; return 1; } return 0; }

void _main() {
    int N;
    cin >> N;
    map<string, int> dicMap;
    rep(i, 0, N){
        string S; cin >> S;
        dicMap[S] ++;
    }

    int maxNum = -1;
    fore(i, dicMap) chmax(maxNum, i.second);
    fore(p, dicMap){
        if (p.second == maxNum) cout << p.first << endl;
    }

}