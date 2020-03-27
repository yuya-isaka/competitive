# フェルマーの小定理，逆元，（繰り返し二乗法）

n,a,b = map(int, input().split())
mod = 10**9 + 7
s = pow(2,n,mod) - 1 # どんな花束の数でもいい時の場合の数（花束を渡さない選択肢はないから，その分は省略）

# nCr
def fur(n,r):
    # ここはnCrの分数の分子と分母を計算
    x,y = 1,1
    for i in range(r):
        x = x*(n-i)%mod
        y = y*(i+1)%mod
    return x * pow(y,mod-2,mod) % mod # フェルマーの小定理を使うことで，割り算のmod計算を掛け算のmod計算にできた(逆元？)

print((s - fur(n,a) - fur(n,b)) % mod)
