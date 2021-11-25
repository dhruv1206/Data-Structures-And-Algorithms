# example of a test directory listing, which can be downloaded [here](https://s3.amazonaws.com/udacity-dsand/testdir.zip):
'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

import os


def find_files(suffix , path):
    if suffix=='':
        return []

    if len(os.listdir(path))==0:
        return []

    path_elements=os.listdir(path)
    files=[files for files in path_elements if '.'+suffix in files]
    folders=[files for files in path_elements if '.' not in files]
    for folder in folders:
        files.extend(find_files(suffix , path+'/'+folder))

    return files

path_base = os.getcwd() + '/testdir'

# Normal Cases:
print(find_files(suffix='c', path=path_base))
# ['t1.c', 'a.c', 'a.c', 'b.c']

print(find_files(suffix='h', path=path_base))
# ['t1.h', 'a.h', 'a.h', 'b.h']

print(find_files(suffix='z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# []
