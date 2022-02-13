import json

f = open('app.json')
words = json.load(f)
f.close
nope = []
yup = []
pos=[]
while(True):
    flag = input("Type:  1 - YES || 2 - NO || 3 - POS: ")
    
    if(flag=="1"):
        b = input("Enter Letters in string:")
        for ch in range(0,len(b)):
            yup.append(b[ch].upper())
        words = [ele for ele in words if all(ch in ele for ch in yup)]

    elif(flag == "2"):
        a = input("Enter Letters not in string:")
        for ch in range(0,len(a)):
            nope.append(a[ch].upper())
        words = [ele for ele in words if all(ch not in ele for ch in nope)]

    else:
        c = input("Enter Letters in order: ")
        c =c.upper()
        for word in words:
            flag2 = True
            for i in range(0,len(c)):
                if(c[i]=="."):
                    continue
                if(c[i]!=word[i]):
                    flag2 = False
            if(flag2):
                pos.append(word)
        words = pos
        pos = []
    
    words.sort(reverse=True)
    for word in words:
        print(word)