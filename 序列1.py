t = input("请输入序列t：")
s = input("请输入序列s：")
a = len(t);
b = len(s);
j = k = 0
while j < a and k < b:
    if s[j] == t[k]:
        j = j + 1
    k = k + 1
if j == a:
    print("yes")
else:
    print("no")