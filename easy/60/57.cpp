#include <iostream>
#include <math.h>

using namespace std;

int main(){
    const int maxNum = 1000;
    const int minNum = 1;
    const int percent8 = 8;
    const int percent10 = 10;
    int A, B;
    cin >> A >> B;
    for(int i=minNum; i<=maxNum; i++){
        if((floor(i*percent8*0.01) == A) && (floor(i*percent10*0.01) == B)){
            cout << i << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}