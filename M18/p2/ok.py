s = '1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM'
x = []
n = []
b = []
c = []
# print(sorted(s))
for i in s:

    if i not in ('1','2','3','4','5','6','7','8','9','0'):
        if i.isupper():
            n.append(i)
            n.sort()
        else:
            x.append(i)
            x.sort()
    else:
        if int(i) % 2 != 0:
            b.append(i)
            b.sort()
        else:
            c.append(i)
            c.sort(+)
r = x + n + b + c
# print(r)
print(''.join(r))

