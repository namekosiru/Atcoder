#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int N, T, A, H;
    cin >> N;
    cin >> T >> A;
    vector<double> degree(N, 0);
    for (int i=0; i<N; i++){
        cin >> H;
        degree[i] = abs(A-(T-H*0.006));
    }
    auto min_index = min_element(degree.begin(), degree.end());
    cout << distance(degree.begin(), min_index)+1 << endl;
    return 0;
}