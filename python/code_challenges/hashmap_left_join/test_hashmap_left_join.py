from hashmap_left_join.hashmap_left_join import hashmap_left_join
from data_structures.hashtable import HashTable
def test_output_all_valid_key():
    ht1=HashTable()
    ht2=HashTable()
    ht1.add('fond','enamored')
    ht1.add('wrath','anger')
    ht1.add('diligent','employed')
    ht2.add('fond','averse')
    ht2.add('wrath','delight')
    ht2.add('diligent','idle')
    actual=hashmap_left_join(ht1,ht2)
    expected=[['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse']]
    assert actual==expected

def test_output_no_matching_key():
    ht1=HashTable()
    ht2=HashTable()
    ht1.add('sara','enamored')
    ht1.add('wrath','anger')
    ht1.add('diligent','employed')
    ht2.add('fond','averse')
    ht2.add('sama','delight')
    ht2.add('diligent','idle')
    actual=hashmap_left_join(ht1,ht2)
    expected=[['wrath', 'anger', 'Null'], ['diligent', 'employed', 'idle'], ['sara', 'enamored', 'Null']]
    assert actual==expected
