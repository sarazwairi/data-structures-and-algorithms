from linked_list.linked_list import LinkedList

class HashTable:

    def __init__(self,size=1024):
        self.size=size
        self._buckets=size*[None]

    def _hash(self,key):
        """
        Arguments: key
        Returns: Index in the collection for that key
        """
        sum=0

        for ch in key:
            sum+=ord(ch)

        index=(sum*7)% self.size
        return index

    def add(self,key,value):
        """
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        """
        index=self._hash(key)

        if not self._buckets[index]:
            self._buckets[index]=LinkedList()
        self._buckets[index].insert([key,value])

    def get(self,key):
        """
        Arguments: key
        Returns: Value associated with that key in the table
        """

        index=self._hash(key)
        if not self._buckets[index]:
            return None
        bucket=self._buckets[index]
        current=bucket.head
        while current:
            if current.value[0]==key:
                return current.value[1]
            current=current.next
        return None

    def contains(self,key):
        """
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        """
        index=self._hash(key)
        if not self._buckets[index]:
            return False
        current=self._buckets[index].head
        while current:
            if current.value[0]==key:
                return True
            else:
                return False

if __name__=="__main__":
    ht=HashTable(10)
    ht.add("sara","33")
    print(ht.get("sara"))
    print(ht.contains("Sara"))
    print(ht.contains("sara"))
    print(ht.get("Sara"))



