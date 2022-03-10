#include <iostream>
#include <map>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    map<string, int> ansMap;
    ansMap["AC"] = 0;
    ansMap["WA"] = 0;

    map<int, int> countWA;
    for(int i=1; i<N+1; i++){
        countWA[i] = 0;
    }
    
    map<int, int> indexMap;
    for(int i=1; i<N+1; i++){
        indexMap[i] = -1;
    }

    for(int i=0; i<M; i++){
        int index;
        string result;
        cin >> index >> result;
        if (indexMap[index] == -1){
            if (result == "WA"){
                countWA[index] += 1;
            }else{
                ansMap["AC"] += 1;
                ansMap["WA"] += countWA[index];
                indexMap[index] = 1;
            }
        }
    }
    cout << ansMap["AC"] << " " << ansMap["WA"] << endl;
    return 0;
}