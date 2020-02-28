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


ll n, h[100100];
ll dp[100100];

int main() {
  cin >> n;
  for(int i = 0; i < n; i++) cin >> h[i];

  for(int i = 0; i < 100100; i++) dp[i] = inf;
  dp[0] = 0;

  for(int i = 0; i < n; i++) {
    dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]));
    dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]));
  }

  cout << dp[n-1] << endl;
}

