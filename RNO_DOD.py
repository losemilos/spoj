n = int(input())
for i in range(0, n):
    m = int(input())
    a = input()
    numbers = list(map(int, a.split()))
    print(sum(numbers))