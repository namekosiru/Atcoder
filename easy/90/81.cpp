#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> a(N);
    for(int i=0; i<N; i++) cin >> a[i];
    int counter = 0;
    for(auto ai: a){
        while (true){
            if(ai%2==0){
                ai = ai/2;
                counter++;
            }
            else break;
        }
    }
    cout << counter << endl;
    return 0;
}