#include <iostream>
#include <set>

using namespace std;

int main() {
    int A, B, K;
    cin >> A >> B >> K;
    set<int> numberSet;
    if (B-A < K){
        for (int i=A; i<=B; i++){
            cout << i << endl;
        }
        return 0;
    }
    
    for (int i=A; i<A+K; i++){
        numberSet.insert(i);
    }
 
    for(int i=B; i>B-K; i--){
        numberSet.insert(i);
    }
    
    for(auto number: numberSet){
        cout << number << endl;
    }
    return 0;
}