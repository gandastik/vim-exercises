#alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
string = "CYtZBsWZaZliYZocWLZlXuZZYWYeYXZsXeZXtXWpXeRYYYd!ZnYeWXoYXasnX,WXWrWPoAdWesnciGenWr"
dic = {}
x = ""
print(f"original string : {string}")
for i in string:
    try:
        dic[i] += 1
    except:
        x += i
        dic[i] = 1
sortedDic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
print(sortedDic)
print("no duplicated char: ", x)
res = ""

for i in range(len(x)):
    if(i % 2 == 0):
        res += x[i]
print("zigzag with skipping every other char: ", res)
res = ""
res2 = ""
for i in range(len(x) // 2):
    res += x[i] + x[len(x) - 1 - i]
    res2 += x[len(x) - 1 - i] + x[i]
print("left then right char", res)
print("right then left char", res2)

s = ""
num = 9
for key in dic.keys():
    if(dic[key] > num):
        continue
    s += key
print()
print(f"unprocessed string at {num}: {s}")
res = ""
for i in range(len(s)):
    if(i % 2 == 0):
        res += s[i]
print("skipping every other char: ", res)
res = ""
res2 = ""
for i in range(len(s) // 2):
    res += s[i] + s[len(s) - 1 - i]
    res2 += s[len(s) - 1 - i] + s[i]
print("left then right char", res)
print("right then left char", res2)
def convert(s):
    ret = ""
    cycleLen = 4
    for i in range(3):
        for j in range(0, len(s) - i, cycleLen):
            ret += s[j + i]
            if (i != 0 and i != 2 and j + cycleLen - i < len(s)):
                ret += s[j + cycleLen - i]
    return ret

print(f"zigzag {convert(s)}")
print(f"zigzag {convert(x)}")


