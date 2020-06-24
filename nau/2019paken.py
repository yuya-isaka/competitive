def main():
    n = int(input())
    # 知りたいのは色の場所ではなく、色の数だから、用意するメモリは3*nでいい
    c = [[0]*3 for _ in range(n)]
    for _ in range(5):
        tmp = input()
        for j, k in enumerate(tmp):
            if k == 'R':
                c[j][0] += 1
            elif k == 'B':
                c[j][1] += 1
            elif k == 'W':
                c[j][2] += 1

    # floatの準備（最小化問題のときは、基本infで初期化すればいい
    inf = float('inf')
    # 配列の用意の仕方
    # 配列数は元の数より＋１する
    dp = [[inf]*3 for _ in range(n+1)]
    # その配列への代入の仕方
    dp[0] = [0]*3

    # したから順番に見る
    for i in range(n):
        for j in range(3):
            for k in range(3):
                if j != k:
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j] + 5 - c[i][k])

    ans = min(dp[n])

    print(ans)




if __name__ == "__main__":
    main()
    pass