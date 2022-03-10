#include <iostream>

using namespace std;

int main() {
    long long  n, a, b;
    cin >> n >> a >> b;
    if ((b-a)%2==0){
        cout << (b-a)/2 << endl;
    }else{
        cout << min((a+b-1)/2, (n*2-a-b+1)/2) << endl;
    }
    return 0;
}