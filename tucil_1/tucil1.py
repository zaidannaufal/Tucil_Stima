from itertools import permutations  

def listtostring(l):
    string = ''
    for x in l:
        string = string + x + ','
    return string[:-1]

def flush(s):
    s = s.replace(',','').replace('+','')
    return ''.join(set(s))

def makedict(s):
    if (len(s) > 10):
        print("Maksimum 10 Huruf Berbeda")
    else:
        d = {}
        for i in range(len(s)):   
            d[s[i]] = '0'
        return d

def changedictvalue(d,l):
    i = 0
    for key in d.keys():
        d[key] = str(l[i])
        i += 1
    return d

def changestringvalue(s,dict):
    for word, initial in dict.items():
        s = s.replace(word, initial)
    return s

def checktotal(l):
    total = 0
    for i in l[:-1]:
        # x = i.replace('+','')
        total = total + int(i)
    # print('-------')
    # print (l)
    # print (total)
    # print (int(l[-1]))
    # print('-------')
    return total == int(l[-1])

def check(l):
    check1 = True
    for i in l:
        if i[0] == '0':
            check1 = False
            break
    return check1 and checktotal(l)

def solution(dict,listsum):
    p = permutations(range(10),len(dict))
    percobaan = 0
    listsum[-2] = listsum[-2].replace('+','')
    for i in list(p):
        listsum_new = []
        dict = changedictvalue(dict,list(i))
        for j in range(len(listsum)):
            listsum_new.append(changestringvalue(listsum[j],dict))
        # print(listsum)
        if check(listsum_new):
            return listsum_new
        else :
            percobaan += 1
    else:
        print ('ga nemu')

    
f = open("tekateki.txt", "r")
listsum = f.read()
print(listsum)
print('solusi:')
listsum = listsum.split('\n')
listsum.pop(-2)
word = listtostring(listsum)
word = flush(word)
worddict = makedict(word)
listsolution = solution(worddict,listsum)
listsolution[-2] = listsolution[-2] + '+'
for i in listsolution[:-1]:
    print(i)
print('------')
print(listsolution[-1])




# x = x.split(',')
# print(x)