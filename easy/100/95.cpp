#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> numbers(3);
    for(int i=0; i<3; i++) cin >> numbers[i];
    int even = 0, odd = 0;
    for(int i=0; i<3; i++){
        if(numbers[i]%2==0) even++;
        else odd++;
    }
    int ans = 0;
    if(odd==2){
        ans++;
        for(int i=0; i<3; i++) if(numbers[i]%2==1) numbers[i]++;
    }else if (even==2) {
        ans++;
        for(int i=0; i<3; i++) if(numbers[i]%2==0) numbers[i]++;
    }
    int max_num = max(numbers[0], max(numbers[1], numbers[2]));

    for(int i=0; i<3; i++){
        ans += (max_num-numbers[i])/2;
    }
    cout << ans << endl;
    return 0;
}