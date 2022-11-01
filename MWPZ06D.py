n = int(input())
for i in range(0,n):
    array = input()
    number = list (map(int, array.split()))
    if ((number[0]-1) % number[1]) == 0:
        print('NIE')
    else:
        print('TAK')
   # print((number[0]-1) % number[1])