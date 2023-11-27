N, P, Q, K = map(int, input().split())
def f(N, P, Q, K):
    z = N // (P * Q)
    k = (K - 1) // z + 1
    mrtb = ((K - 1) % z) // Q + 1
    return k, mrtb
print(*f(N, P, Q, K))
?