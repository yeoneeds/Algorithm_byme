t = int(input())

for i in range(1,t+1):
    s = list(map(int, input().split()))
    print(f"#{i} {round(sum(s)/10)}")
