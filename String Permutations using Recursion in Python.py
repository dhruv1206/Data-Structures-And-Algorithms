'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''


def list_permutaions(s):
    l=[i for i in s ]
    if len(l)==1:
        return [l]

    result=[]


    for i in range (len(l)):
        other = l[:i]+l[i+1:]
        other_permutations=list_permutaions(other)
        for permutations in other_permutations:
            result.append([l[i]]+permutations)
    return result

print(list_permutaions("ab"))
print(list_permutaions("abc"))
print(list_permutaions("abcd"))

