#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int numbers[N];
    for(int i=0; i<N; i++) cin >> numbers[i];
    int index = 1, count = 0;
    for(int i=0; i<N; i++){
        if(index==numbers[i]){
            index++;
        }else{
            count++;
        }
    }
    if (count == N){
        cout << -1 << endl;
        return 0;
    }
    cout << count << endl;

    return 0;
}