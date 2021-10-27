'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''


def list_permutaions(l):
    if len(l)==1:
        return [l]

    result=[]


    for i in range (len(l)):
        other = l[:i]+l[i+1:]
        other_permutations=list_permutaions(other)
        for permutations in other_permutations:
            result.append([l[i]]+permutations)
    return result

print(list_permutaions([]))
print(list_permutaions([0]))
print(list_permutaions([0,1]))
print(list_permutaions([0,1,2]))

