#첫째 줄에는 별 2×N-1개, 둘째 줄에는 별 2×N-3개, ..., N번째 줄에는 별 1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다.
import sys
n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    print(' '* (n-i) + '*'*(2*i-1))
