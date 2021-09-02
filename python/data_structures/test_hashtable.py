from hashtable import HashTable
import pytest


    # Adding a key/value to your hashtable results in the value being in the data structure
    # Retrieving based on a key returns the value stored
    # Successfully returns null for a key that does not exist in the hashtable
    # Successfully handle a collision within the hashtable
    # Successfully retrieve a value from a bucket within the hashtable that has a collision
    # Successfully hash a key to an in-range value
def test_add_get():
    ht=HashTable()
    ht.add("sara","33")
    assert ht.get("sara")=="33"

def test_add_contain():
    ht=HashTable()
    ht.add("sara","33")
    assert ht.contains("sara")==True

def test_no_key():
    ht=HashTable()
    ht.add("sara","33")
    assert ht.contains("Sara")==False


def test_no_value():
    ht=HashTable()
    ht.add("sara","33")
    assert ht.get("Sara")==None

def test_collisin():
    ht=HashTable()
    first=ht._hash("33")
    second=ht._hash("33")
    assert first==second

def test_in_range():
    ht=HashTable()
    actual=ht._hash("33")
    assert 0<=actual<ht.size
