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

ll h, w;
vector<string> a;

ll dp[1100][1100];

void add(ll &a, ll b){
    a += b;
    if(a >= mod) a -= mod;
}

int main() {
    cin >> h >> w;
    a.resize(h);
    for(int i = 0; i < h; i++) cin >> a[i];

    dp[0][0] = 1;
    
    for(int i = 0; i < h; i++){
        for(int j = 0; j < w; j++){
            if(i+1 < h && a[i+1][j] == '.') add(dp[i+1][j], dp[i][j]);
            if(j+1 < w && a[i][j+1] == '.') add(dp[i][j+1], dp[i][j]); 
        }
    }

    cout << dp[h-1][w-1] << endl;
}