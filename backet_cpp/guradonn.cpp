#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <utility>
#include <cstdlib>
#include <queue>
#include <stack>
#include <iomanip>
#include <cstdio>
#include <map>
#include <list>
#include <stdio.h>
#include <sstream>
using namespace std;
using ll = long long;
using P = pair<ll,ll>;
#define all(x) (x).begin(), (x).end()
#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );
//ll gcd(ll a, ll b){return b?gcd(b,a%b):a;}
//ll lcm(ll x, ll y) {return x / gcd(x, y) * y;}
const int dx[4] = {1,0,-1,0};
const int dy[4] = {0,1,0,-1};
const ll mod = 1e9 + 7;
const ll inf = 1LL << 60;
const long double pi = 3.14159265358979323846;

// ****************************************CODE***************************************//

string s, t;
ll dp[3100][3100];

int main() {
    cin >> s >> t;

    for(int i = 0; i < s.size(); i++){
        for(int j = 0; j < t.size(); j++){
            if(s[i] == t[j]) dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1);
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j]);
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1]);
        }
    }

    string res = "";
    ll i = s.size(), j = t.size();
    while(i > 0 && j > 0) {
        if(dp[i-1][j] == dp[i][j]) i--;
        else if(dp[i][j-1] == dp[i][j]) j--;
        else {
            res = s[i-1] + res;
            i--; 
            j--;
        }
    }

    cout << res << endl;
}