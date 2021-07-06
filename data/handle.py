import os

def getName(num):
    strTmp = []
    strRes = ''

    while(num / 10):
        strTmp.append(num % 10)
        num = num / 10
    strTmp.append(num)
    n = len(strTmp)
    for i in range(0,5-n):
        strRes = strRes + '0'
    for i in range(n-1,-1,-1):
        strRes = strRes + str(strTmp[i])
    return strRes

file_object = open('rgb.txt','w')
Ostr = ''
num = len(os.listdir('rgb'))
for i in range(1,num+1):
    name = getName(i)
    Ostr = Ostr + name + ' rgb/' + name + '.png\n'
file_object.writelines(Ostr)
file_object.close()
