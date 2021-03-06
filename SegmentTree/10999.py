import sys
input = sys.stdin.readline

def init(si, ei, node=1):
    if si == ei:
        tree[node] = arr[si]
        return tree[node]
    else:
        mid = (si + ei) // 2
        tree[node] = init(si, mid, node * 2) + init(mid + 1, ei, node*2 + 1)
        return tree[node]


def query(qli, qri, si, ei, node=1):
    update_lazy(si, ei, node)
    if qli > ei or qri < si:
        return 0
    if qli <= si and ei <= qri:
        return tree[node]

    mid = (si + ei) // 2
    return query(qli, qri, si, mid, node * 2) + query(qli, qri, mid + 1, ei, node*2 + 1)


def update_lazy(si, ei, node):
    if lazy[node] != 0:
        tree[node] += (ei - si + 1)*lazy[node]

        if si != ei:
            lazy[node*2] += lazy[node]
            lazy[node*2 + 1] += lazy[node]
        lazy[node] = 0


def update_range(qli, qri, v, si, ei, node=1):
    update_lazy(si, ei, node)
    if ei < qli or si > qri:
        return

    if qli <= si and ei <= qri:
        tree[node] += (ei-si+1)*v
        if si != ei:
            lazy[node*2] += v
            lazy[node*2 + 1] += v
        return

    mid = (si + ei) // 2
    update_range(qli, qri, v, si, mid, node * 2)
    update_range(qli, qri, v, mid + 1, ei, node*2 + 1)
    tree[node] = tree[node*2] + tree[node*2 + 1]


N, M, K = map(int, input().split())
tree = [0] * (4 * N)
lazy = [0] * (4 * N)
arr = []
for i in range(N):
    arr.append(int(input()))

init(0, N - 1)
for _ in range(M + K):
    l = list(map(int, input().split()))
    if len(l) == 4:
        a, b, c, d = l
        b -= 1
        c -= 1
        update_range(b, c, d, 0, N - 1)
    else:
        a, b, c = l
        print(query(b, c, 1, N))
