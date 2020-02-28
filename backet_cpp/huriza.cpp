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

ll n, m;
vector<vector<ll> > g;
vector<ll> num;
ll dp[100100];

int main() {
    cin >> n >> m;
    g.assign(n, vector<ll>());
    num.assign(n, 0);
    for(int i = 0; i < m; i++){
        ll x, y; cin >> x >> y; x--; y--; g[x].push_back(y); num[y]++;
    }

    queue<ll> que;
    for(int i = 0; i < n; i++) if(num[i] == 0) que.push(i);

    while(!que.empty()){
        ll i = que.front(); que.pop();
        for(auto j: g[i]){
            num[j]--;
            if(num[j] == 0) {
                que.push(j);
                dp[j] = max(dp[j], dp[i] + 1);
            }
        }
    }

    ll res = 0;
    for(int i = 0; i < n; i++) res = max(res, dp[i]);
    cout << res << endl;
}