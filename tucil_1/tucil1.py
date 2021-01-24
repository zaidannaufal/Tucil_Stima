from itertools import permutations  
import timeit

def listtostring(l):
    string = ''
    for x in l:
        string = string + x
    return string

def makedict(s):
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

def check(l):
    for i in l:
        if i[0] == '0':
            return False
    total = 0
    for i in l[:-1]:
        total = total + int(i)
    return total == int(l[-1])

def solution(dict,listsum):
    p = permutations(range(10),len(dict))
    tries = 1
    for i in list(p):
        listsum_new = []
        dict = changedictvalue(dict,list(i))
        for j in range(len(listsum)):
            listsum_new.append(changestringvalue(listsum[j],dict))
        if check(listsum_new):
            listsum_new.append(str(tries))
            return listsum_new
        else :
            tries +=1
    else:
        print('tidak ditemukan solusi')
        return []

def crypt(tekateki):
    print("Soal :")
    print(tekateki)
    print('\nSolusi :')
    tekateki = tekateki.replace(" ","").replace('+','').split('\n')
    tekateki.pop(-2)
    word = ''.join(set(listtostring(tekateki)))
    if len(word) <=10:
        worddict = makedict(word)
        start=timeit.default_timer()
        listsolution = solution(worddict,tekateki)
        stop=timeit.default_timer()
        if listsolution: 
            tries = listsolution[-1]
            listsolution = listsolution[:-1]
            whitespace = ' '
            for i in listsolution[:-2]:
                wlenght = len(listsolution[-1]) - len(i)
                print(whitespace*wlenght+i)
            print(whitespace *(len(listsolution[-1]) - len(listsolution[-2])) + listsolution[-2] + '+')
            print('------')
            print(listsolution[-1])
            print(f"\nTotal percobaan: {tries}")
            print("Waktu diperlukan: " + "{:.2f}".format(stop-start) +" seconds\n")
    else:
        print('Tidak terdapat solusi dikarenakan jumlah huruf berbeda lebih dari 10')

if __name__ == "__main__":
    f = open("tekateki.txt", "r")
    tekateki = f.read()
    tekateki = tekateki.split('\n\n')
    for i in range(len(tekateki)):
        crypt(tekateki[i])