// BOJ 11047
#include <iostream>
#include <stack>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int N,K,cnt = 0;
    stack<int> st;
    cin >> N >> K;
    for(int i=0; i<N; i++){
        int a; cin >> a;
        st.push(a);
    }

    for(int i=0; i<N; i++){
        cnt += K / st.top();
        K %= st.top();
        st.pop();
    }

    cout << cnt << "\n";
}