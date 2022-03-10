#include <iostream>
#include<math.h>

using namespace std;

int main() {
    int N;
    cin >> N;
    int a[N];
    int subtractNum = 1;
    for(int i=0; i<N; i++) cin >> a[i];
    for(int i=0; i<N; i++){
        if(a[i]%2==0) subtractNum *= 2;
        else subtractNum *= 1;
    }
    cout << pow(3, N) - subtractNum << endl;
    return 0;
}