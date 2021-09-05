from data_structures.hashtable import HashTable
import re

def repeated_word(str):
    ht=HashTable()
    list_string=re.findall(r'\w+', str)
    if str=='':
        return 'no string'
    for word in list_string:
        lower_word=word.lower()
        if ht.contains(lower_word):
            return lower_word
        else:
            ht.add(lower_word,lower_word)
    return None

if __name__=='__main__':
    ht=HashTable()
    str="Once upon a time, there was a brave princess who..."
    repeated_word=repeated_word(str)
    print (repeated_word)

