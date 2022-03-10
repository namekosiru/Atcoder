#include <iostream>

using namespace std;

int main() {
    long long  N;
    cin >> N;
    long power = 1;
    for(int i=1; i<N+1; i++) {
        power *= i;
        power %= 1000000007;
    }
    cout << power << endl;
    
    return 0;
}