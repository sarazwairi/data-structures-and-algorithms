# Hashtables


## Challenge
Implement a Hashtable Class with the following methods:

add()
get()
contains()
hash()

## Approach & Efficiency

BigO:

Time:O(1)

Space:O(n)

## API


    * add
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

    * get
        Arguments: key
        Returns: Value associated with that key in the table

    * contains
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        
    * hash
        Arguments: key
        Returns: Index in the collection for that key
