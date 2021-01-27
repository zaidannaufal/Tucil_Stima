import timeit

def listtoint(l):
    i = len(l)-1
    integer = 0
    for x in l:
        integer = integer + x * 10**i
        i-=1
    return integer

def permutations(s,len):
    for  i in range(len-2,-1,-1):
        if ( s[i] < s[i+1] ):
            break;
    if ( i < 0 ):
        return 0
    for j in range(len-1,i-1,-1):
        if ( s[j] > s[i] ):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            break
    i= i + 1
    k = len-1
    while(k>i):
        temp = s[i]
        s[i] = s[k]
        s[k] = temp
        i+=1
        k-=1
    return s;

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
    p = [0,1,2,3,4,5,6,7,8,9]
    tries = 1
    while int(listtoint(p)) != 9876543210:
        listsum_new = []
        dict = changedictvalue(dict,p[10-len(dict):])
        for j in range(len(listsum)):
            listsum_new.append(changestringvalue(listsum[j],dict))
        if check(listsum_new):
            listsum_new.append(str(tries))
            return listsum_new
        else :
            tries +=1
        p = permutations(p,10)
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
        listsolution = solution(worddict,tekateki)
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
            
    else:
        print('Tidak terdapat solusi dikarenakan jumlah huruf berbeda lebih dari 10')

if __name__ == "__main__":
    namafile = "tekateki.txt"
    f = open(f"./test/{namafile}", "r")
    tekateki = f.read()
    tekateki = tekateki.split('\n\n')
    for i in range(len(tekateki)):
        start=timeit.default_timer()
        crypt(tekateki[i])
        stop=timeit.default_timer()
        print("Waktu diperlukan: " + "{:.2f}".format(stop-start) +" seconds\n")