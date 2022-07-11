#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    int N, M, cnt = 0;
    map<string, int> dict;
    vector<string> ans;
    cin.tie(0); cout.tie(0);
    cin >> N >> M;
    
    for(int i=0; i<N+M; i++){
        string s;
        cin >> s;
        dict[s]++;
        if(dict[s] == 2) ans.push_back(s);
    }

    sort(ans.begin(), ans.end());

    cout << ans.size() << "\n";
    for (int i=0; i<ans.size(); i++) {
        cout << ans[i] << "\n";
	}     
    
    return 0;
}