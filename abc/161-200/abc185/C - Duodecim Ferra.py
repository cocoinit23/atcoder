from scipy.special import comb

l = int(input())

ans = comb(l - 1, 11, exact=True)
print(ans)
