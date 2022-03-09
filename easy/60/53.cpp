#include<iostream>

using namespace std;

int deg[60];

int main(){
    int N, M, a, b;
    cin >> N >> M;
    for (int i=0; i<M; i++){
        cin >> a >> b;
        deg[a-1]++; deg[b-1]++;
    }
    for (int i=0; i<N; i++) cout << deg[i] << endl;
    return 0;
}