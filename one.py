alphabet = "abcdefghigklmnoprstuvwhxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()-_=+\\{}[]"
strings =open('./flag.txt').read()
res={}
for i in alphabet:
    counts = strings.count(i)
    i = '{0}'.format(i)
    res[i] = counts
rew = sorted(res.items(),key=lambda item:item[1],reverse=True)
for data in rew:
    print(data)
for i in rew:
    flag = str(i[0])
    print(flag[0],end="")