def acc_sum(array):
    for i in range(1, len(array)):
        array[i] += array[i-1]

def bin_search(e, array, l, r, a):
    middle = (l+r)//2
    if array[middle] == e or middle == a: return middle+1
    if l >= r: return r+1
    if array[middle] < e:
        return bin_search(e, array, middle+1, r, middle)
    return bin_search(e, array, l, middle, middle)

qp = int(input())
pilhas = list(map(int, input().split()))
qw = int(input())
worms = list(map(int, input().split()))

acc_sum(pilhas)
for i in worms:
    a = bin_search(i, pilhas, 0, qp-1, -1)
    print(a)