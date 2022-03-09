#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int N;
    cin >> N;
    vector<string> dic(N); 
    for(int i=0; i<N; i++){
        cin >> dic[i];
    }
    for (auto character: dic){
        if (count(dic.begin(), dic.end(), character) >= 2){
            cout << "No" << endl;
            return 0;
        }
    }
    int i_length, i1_length;
    for (int i=0; i<N-1; i++){
        i_length = dic[i].length();
        if (dic[i][i_length-1] != dic[i+1][0]){
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;

    return 0;
}