abc = lambda aa, bb, cc, dd: max(aa, bb, cc, dd)
print(abc(1, 3, 5, 9))
abc = lambda aa, bb, cc, dd: (aa, bb, cc, int(dd))
print(min(abc(1, 3, 4, "9")))


target = [1, 3, 4, "9"]
abc = lambda x:int(x)
print(min(list(map(abc, target))))

# 公式
# lambda arguments : expression
abc = lambda x : x
print(abc([1,2,3]))

print(list(map(lambda i:i**2,range(1,11))))