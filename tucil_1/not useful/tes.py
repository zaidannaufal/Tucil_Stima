# s = [1,2,3,4,5,6]

# def listtoint(l):
#     i = len(l)-1
#     integer = 0
#     for x in l:
#         integer = integer + x * 10**i
#         i-=1
#     return integer

# def permutations(s,len):
#     for  i in range(len-2,-1,-1):
#         if ( s[i] < s[i+1] ):
#             break;
    
#     if ( i < 0 ):
#         return 0
    
#     for j in range(len-1,i-1,-1):
#         if ( s[j] > s[i] ):
#             temp = s[i]
#             s[i] = s[j]
#             s[j] = temp
#             break
    
#     i= i + 1
#     k = len-1
#     while(k>i):
#         temp = s[i]
#         s[i] = s[k]
#         s[k] = temp
#         i+=1
#         k-=1

#     return s;



# while int(listtoint(s)) != 654321:
#      s = permutations(s,4)
#      print(s)
# # print(s)
# # s = permutations(s,len(s))
# # print(s)

s = [1,2,3,4,5,6,7,8,9,0]
s = s[10-7:]
print(s)